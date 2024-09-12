import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
from asgiref.sync import async_to_sync



class MyNotification(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connection established now...", event)

        # Add the channel to the notification group
        await self.channel_layer.group_add("notification", self.channel_name)

        # Accept the WebSocket connection
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("WebSocket data received now", event)

        # Send a message to the notification group
        await self.channel_layer.group_send(
            "notification",
            {
                "type": "notification.send",
                "message": event['text']
            }
        )

    async def notification_send(self, event):
        # Send the message to WebSocket
        await self.send({
            "type": "websocket.send",
            "text": event['message']
        })

    async def websocket_disconnect(self, event):
        print("Disconnected now...", event)

        # Discard the channel from the notification group
        await self.channel_layer.group_discard("notification", self.channel_name)
