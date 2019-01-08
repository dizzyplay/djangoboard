from channels.generic.websocket import AsyncWebsocketConsumer
import json


def get_groupname():
    return 'connected_group'


class NotiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.connected_group = get_groupname()
        await self.channel_layer.group_add(
            self.connected_group,
            self.channel_name
        )

        print('successfully connected')
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.connected_group,
            self.channel_name
        )

    async def broadcast_new_post(self, event):
        print(event)

        await self.send(text_data=json.dumps({
            'message':'새로운 글이 올라왔습니다.',

        })
        )
