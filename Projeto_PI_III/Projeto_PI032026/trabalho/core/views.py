from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .models import ItemPedido, Cliente, Pedido
from .serializers import PedidoSerializer
from .forms import ClienteForm
from produtos.models import Produto
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views.decorators.http import require_POST


# Função para filtrar pedidos por data
def filtrar_pedidos_por_data(request, queryset):
    data_inicio = request.GET.get("data_inicio")
    data_fim = request.GET.get("data_fim")

    if data_inicio:
        queryset = queryset.filter(data_criacao__date__gte=data_inicio)

    if data_fim:
        queryset = queryset.filter(data_criacao__date__lte=data_fim)

    return queryset, data_inicio, data_fim


def pedido_list(request):
    pedidos = Pedido.objects.all().order_by("-data_criacao")
    return render(request, "core/pedido_list.html", {"pedidos": pedidos})


@csrf_exempt
def adicionar_ao_carrinho(request, produto_id):
    if request.method == "POST":
        produto = get_object_or_404(Produto, id=produto_id)
        quantidade = int(request.POST.get("quantidade", 1))

        if "carrinho" not in request.session:
            request.session["carrinho"] = []

        carrinho = request.session["carrinho"]

        for item in carrinho:
            if item["produto_id"] == produto_id:
                item["quantidade"] += quantidade
                break
        else:
            carrinho.append(
                {
                    "produto_id": produto_id,
                    "nome": produto.nome,
                    "preco": str(produto.preco),
                    "quantidade": quantidade,
                }
            )

        request.session.modified = True
        messages.success(request, f"{produto.nome} adicionado ao carrinho!")
        return redirect("ver_carrinho")


def criar_pedido(request):
    """
    Exibe a tela inicial para criação de um pedido
    (normalmente lista de produtos ou redirecionamento)
    """
    return render(request, "core/criar_pedido.html")


def cadastro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect("dashboard")  # ou outra página que você preferir
    else:
        form = ClienteForm()

    return render(request, "core/cadastro_cliente.html", {"form": form})


def ver_carrinho(request):
    carrinho = request.session.get("carrinho", [])
    total = sum(float(item["preco"]) * item["quantidade"] for item in carrinho)

    return render(request, "core/carrinho.html", {"carrinho": carrinho, "total": total})


def finalizar_pedido(request):
    carrinho = request.session.get("carrinho", [])

    if not carrinho:
        messages.error(request, "Seu carrinho está vazio!")
        return redirect("ver_carrinho")

    total = sum(float(item["preco"]) * item["quantidade"] for item in carrinho)

    if request.method == "POST":
        cliente = request.POST.get("cliente")
        mesa = request.POST.get("mesa")
        observacoes = request.POST.get("observacoes")

        # ✅ Criar pedido
        pedido = Pedido.objects.create(
            cliente=cliente, mesa=mesa, observacoes=observacoes, valor_total=total
        )

        # ✅ Criar itens do pedido
        itens = []
        for item in carrinho:
            produto = Produto.objects.get(id=item["produto_id"])
            item_pedido = ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=item["quantidade"],
                preco_unitario=produto.preco,
            )
            itens.append(item_pedido)

        # 🔔 NOTIFICAR KDS EM TEMPO REAL (LOCAL CORRETO)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "kds_pedidos",
            {
                "type": "pedido_evento",
                "data": {
                    "tipo": "pedido_novo", 
                    "numero": pedido.numero_pedido,       # Visual
                    "id": pedido.id,           #ID REAL
                    "pedido": pedido.numero_pedido,
                    "mesa": pedido.mesa,
                    "status": pedido.status,
                    "itens": [f"{i.quantidade}x {i.produto.nome}" for i in itens],
                },
            },
        )

        # ✅ Limpa carrinho
        del request.session["carrinho"]
        messages.success(request, f"Pedido {pedido.numero_pedido} criado com sucesso!")

        return redirect("lista_produtos")

    return render(
        request, "core/finalizar_pedido.html", {"carrinho": carrinho, "total": total}
    )


@require_POST
def atualizar_status_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    novo_status = request.POST.get("status")

    if novo_status in dict(Pedido.STATUS_CHOICES):
        pedido.status = novo_status
        pedido.save()

        # 🔔 Notificar KDS (status mudou)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "kds_pedidos",
            {
                "type": "pedido_evento",
                "data": {
                    "tipo": "pedido_status_atualizado",
                    "id": pedido.id,
                    "status": pedido.status,
                },
            }
        )

    return redirect("kds")



def lista_produtos(request):
    context = {
        "lanches": Produto.objects.filter(
            categoria="lanche", oculto=False, disponivel=True
        ),
        "bebidas": Produto.objects.filter(
            categoria="bebida", oculto=False, disponivel=True
        ),
        "sobremesas": Produto.objects.filter(
            categoria="sobremesa", oculto=False, disponivel=True
        ),
        "porcoes": Produto.objects.filter(
            categoria="porcao", oculto=False, disponivel=True
        ),
        "combos": Produto.objects.filter(
            categoria="combo", oculto=False, disponivel=True
        ),
        "pasteis": Produto.objects.filter(
            categoria="pastel", oculto=False, disponivel=True
        ),
    }
    return render(request, "core/lista_produtos.html", context)


def cancelar_carrinho(request):
    if "carrinho" in request.session:
        del request.session["carrinho"]
        messages.info(request, "Carrinho cancelado com sucesso. ")
    return redirect("lista_produtos")


def dashboard(request):
    hoje = timezone.now().date()
    pedidos = Pedido.objects.all()

    data_inicio = request.GET.get("data_inicio")
    data_fim = request.GET.get("data_fim")
    faturamento_total = pedidos.aggregate(total=Sum("valor_total"))["total"] or 0

    quantidade_pedidos = pedidos.count()

    clientes_count = Cliente.objects.count()

    faturamento_dia = (
        Pedido.objects.filter(data_criacao__date=hoje).aggregate(
            total=Sum("valor_total")
        )["total"]
        or 0
    )

    faturamento_mes = (
        Pedido.objects.filter(
            data_criacao__month=hoje.month, data_criacao__year=hoje.year
        ).aggregate(total=Sum("valor_total"))["total"]
        or 0
    )

    faturamento_ano = (
        Pedido.objects.filter(data_criacao__year=hoje.year).aggregate(
            total=Sum("valor_total")
        )["total"]
        or 0
    )

    dias, valores = [], []
    for i in range(6, -1, -1):
        dia = hoje - timedelta(days=i)
        total = (
            Pedido.objects.filter(data_criacao__date=dia).aggregate(
                total=Sum("valor_total")
            )["total"]
            or 0
        )

        dias.append(dia.strftime("%d/%m"))
        valores.append(float(total))

    top_produtos = (
        ItemPedido.objects.filter(pedido__status="finalizado")
        .values("produto__nome")
        .annotate(total_vendido=Sum("quantidade"))
        .order_by("-total_vendido")[:5]
    )

    context = {
        "faturamento_total": faturamento_total,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "quantidade_pedidos": quantidade_pedidos,
        "clientes_count": clientes_count,
        "faturamento_dia": faturamento_dia,
        "faturamento_mes": faturamento_mes,
        "faturamento_ano": faturamento_ano,
        "dias": dias,
        "valores": valores,
        "labels_produtos": [p["produto__nome"] for p in top_produtos],
        "valores_produtos": [p["total_vendido"] for p in top_produtos],
    }

    return render(request, "core/dashboard.html", context)


def kds(request):
    pedidos = Pedido.objects.filter(status__in=["pendente", "preparando"]).order_by(
        "data_criacao"
    )

    return render(request, "core/kds.html", {"pedidos": pedidos})
