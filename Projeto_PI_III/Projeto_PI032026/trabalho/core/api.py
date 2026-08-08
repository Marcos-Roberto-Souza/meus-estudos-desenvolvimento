# core/api.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Pedido
from core.serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @action(detail=True, methods=["post"])
    def atualizar_status(self, request, pk=None):
        pedido = self.get_object()
        novo_status = request.data.get("status")

        if novo_status in dict(Pedido.STATUS_CHOICES):
            pedido.status = novo_status
            pedido.save(update_fields=["status"])
            return Response({"status": "success"})

        return Response(
            {"status": "error", "message": "Status inválido"},
            status=status.HTTP_400_BAD_REQUEST
        )
