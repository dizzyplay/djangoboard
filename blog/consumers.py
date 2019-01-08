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
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.connected_group,
            self.channel_name
        )

    async def notification_new(self, event):
        await self.send(text_data=json.dumps({
            'message': '새로운 글이 등록되었습니다',
            'title': event['title'],
            'post_id': event['post_id']
            })
        )
