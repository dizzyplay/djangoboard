from django.urls import re_path
from . import views


app_name = 'blog'


urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post_detail/(?P<pk>\d+)', views.post_detail, name='post_detail'),
    re_path(r'^post_new/$', views.post_new, name="post_new"),
]