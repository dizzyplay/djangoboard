from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=13, unique=True)
    status = models.BooleanField()

    def __str__(self):
        return self.nickname


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, status=False)
    instance.profile.save()
