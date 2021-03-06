from django.urls import re_path, include
from . import views


app_name = 'board'


urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post_new/$', views.post_new, name="post_new"),
    re_path(r'^post_detail/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    re_path(r'^post_delete/(?P<pk>\d+)/', views.post_delete, name='post_delete'),
    re_path(r'^post_edit/(?P<pk>\d+)/', views.post_edit, name='post_edit'),

    re_path(r'^api/', include('board.api.urls', namespace='board_api')),
]