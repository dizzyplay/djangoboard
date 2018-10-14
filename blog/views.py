from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
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
