from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ImageListSerializer
from .models import Image


class ImageAPIView(APIView):
    serializer_class = ImageListSerializer

    def get(self, request):
        qs = Image.objects.all()
        serializer = ImageListSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImageListSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response()


image_upload = ImageAPIView.as_view()
