from rest_framework import serializers
from .models import Image


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('post','photo',)
