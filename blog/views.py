from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Category
from .forms import PostForm

# Create your views here.


def post_list(request):
    category = request.GET.get('category', None)
    if category:
        try:
            category_q = Category.objects.get(title=category)
            qs = Post.objects.filter(category=category_q)
        except ObjectDoesNotExist:
            qs = Post.objects.all()
    else:
        qs = Post.objects.all()
    return render(request, 'blog/post_list.html',
                  {
                      "qs": qs
                  })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/post_detail.html', {
        "post": post
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form
    })
