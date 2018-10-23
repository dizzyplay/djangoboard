from django.urls import re_path, path
from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.PostListAPIView.as_view(), name='post_list'),
    re_path(r'^(?P<pk>\d+)/$', views.PostDetailAPIView.as_view(), name='post_detail')
]
