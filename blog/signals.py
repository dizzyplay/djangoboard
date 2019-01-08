from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Post
from .consumers import get_groupname


@receiver(post_save, sender=Post)
def test(sender, created, instance, **kwargs):
    title = instance.title
    print(title)
    if created:
        channel_layer = get_channel_layer()
        group_name = get_groupname()
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'notification.new',
                'title': instance.title,
                'post_id': instance.id,
            }

        )
