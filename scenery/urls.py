from django.urls import re_path
from . import views

app_name = 'scenery'

urlpatterns = [
    re_path('', views.main_view, name='main_view'),
]