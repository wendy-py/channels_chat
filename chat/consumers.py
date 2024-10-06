import json
from channels.generic.websocket import AsyncWebsocketConsumer

# channels' consumers is like django's views
class Chat(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # receive from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # send to room group
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat_receive', 'message': message}
        )

    # receive from room group
    async def chat_receive(self, event):
        message = event["message"]

        # send to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
