from django.shortcuts import render
from . import forms


# Create your views here.


def image_upload(request):
    form = forms.ImageForm()
    if request.method == 'POST':
        post_pk = request.POST.get('pk')

    return render(request, 'image/upload_photo.html', {
        'form': form,
    })
