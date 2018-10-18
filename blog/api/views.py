from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from blog.models import Post


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostListAPIView.as_view()
