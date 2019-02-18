from django.db import models
from board.models import Post

# Create your models here.


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='image/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.photo)
