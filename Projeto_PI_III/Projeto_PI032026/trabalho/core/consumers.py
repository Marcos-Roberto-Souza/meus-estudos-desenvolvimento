import json
from channels.generic.websocket import AsyncWebsocketConsumer


class KDSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "kds_pedidos"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def pedido_novo(self, event):
        await self.send(text_data=json.dumps(event["data"]))

    async def pedido_status_atualizado(self, event):
        await self.send(text_data=json.dumps(event["data"]))


    async def pedido_evento(self, event):
        await self.send(text_data=json.dumps(event["data"]))
