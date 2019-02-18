from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


def main(request):
    return HttpResponse('<h1>Hello</h1>')


urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('board/', include('board.urls', namespace='board')),
    path('users/', include('users.urls', namespace='users')),
    path('image/', include('image.urls', namespace='image')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
