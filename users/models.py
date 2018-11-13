from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nickname
