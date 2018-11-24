from django.urls import re_path
from . import views

app_name = 'image'


urlpatterns = [
    re_path(r'^upload/', views.image_upload, name='image_upload')
]