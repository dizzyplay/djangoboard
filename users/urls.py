from django.urls import re_path
from . import views

app_name = 'users'


urlpatterns = [
    re_path(r'^profile/$', views.user_profile, name='user_profile'),
    re_path(r'^logout/$',views.logout_view, name='logout'),
    re_path(r'^login/$', views.login_view, name='login'),
    re_path(r'^signup/$', views.sign_up, name='sign_up'),
]