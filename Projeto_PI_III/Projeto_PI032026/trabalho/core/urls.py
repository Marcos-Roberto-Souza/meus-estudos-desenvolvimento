from .views import dashboard
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from core.api import PedidoViewSet
from core import views
router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('criar-pedido/', views.criar_pedido, name='criar_pedido'),
    path('cadastro-cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('carrinho/cancelar/', views.cancelar_carrinho, name='cancelar_carrinho'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kds/', views.kds, name='kds'),
    path('pedido/<int:pk>/status/', views.atualizar_status_pedido, name='atualizar_status_pedido'),
    path('api/', include(router.urls)),
]