from django.contrib import admin
from .models import Produto
from .forms import ProdutoForm

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    form = ProdutoForm
    list_display = ('nome', 'categoria', 'preco', 'disponivel', 'oculto')
    list_filter = ('categoria', 'disponivel', 'oculto')
    search_fields = ('nome', 'descricao')
    actions = ['ocultar_produtos', 'reativar_produtos']
    fields = ('nome', 'descricao', 'preco', 'categoria', 'imagem', 'disponivel', 'oculto')