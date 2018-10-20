from .serializers import PostSerializer, PostCreateSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

post_list = PostListAPIView.as_view()
