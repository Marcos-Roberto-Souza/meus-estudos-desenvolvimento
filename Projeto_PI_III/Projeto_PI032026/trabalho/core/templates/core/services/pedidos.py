from core.models import Pedido


def atualizar_status_pedido(pedido: Pedido, novo_status: str) -> bool:
    if novo_status in dict(Pedido.STATUS_CHOICES):
        pedido.status = novo_status
        pedido.save(update_fields=["status"])
        return True
    return False