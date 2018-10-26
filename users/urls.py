from django.urls import re_path
from django.conf import settings
from . import views

app_name = 'users'


urlpatterns = [
    re_path(r'^profile/$', views.user_profile, name='user_profile'),
    re_path(r'^logout/$',views.logout_view, name='logout'),
]