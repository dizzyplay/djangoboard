from django.urls import re_path
from . import views

app_name = 'consulting'


urlpatterns = [
    re_path(r'^$', views.main_view, name='main_view'),
    re_path(r'^test/$', views.test_view, name='test_view')
]