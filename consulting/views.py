from django.shortcuts import render, redirect
from .forms import ProductRequestForm


def main_view(request):
    return render(request, './consulting/project_requirements_form.html')


def test_view(request):
    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulting:main_view')
    else:
        form = ProductRequestForm()

    return render(request, './consulting/test.html',{
        'form': form
    })

