from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def short_date(self):
        return self.created_at.strftime("%y/%m/%d")

    class Meta:
        ordering=['-id']




