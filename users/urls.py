from django.urls import re_path
from . import views

app_name = 'users'


urlpatterns = [
    re_path(r'^profile/$', views.user_profile, name='user_profile'),
]