from django.shortcuts import render, redirect
from django.forms import model_to_dict

from .forms import ProductRequestForm
from .tasks import send_product_request_mail


def main_view(request):
    return render(request, './consulting/project_requirements_form.html')


def test_view(request):
    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        if form.is_valid():
            post = form.save()
            post_dict = model_to_dict(post)
            post_dict['get_request_category_display'] = post.get_request_category_display()
            post_dict['short_date'] = post.short_date()
            # send email async
            send_product_request_mail(post_dict)

            return redirect('consulting:test_view')
    else:
        form = ProductRequestForm()
    return render(request, './consulting/test.html', {
        'form': form
    })
