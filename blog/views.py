from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Category
from .forms import PostForm
from .context_processors import category_context


def post_list(request):
    category = category_context(request)['category_title']
    if category:
        try:
            category_q = Category.objects.get(title=category)
            qs = Post.objects.filter(category=category_q)
        except ObjectDoesNotExist:
            print('object does not exist!!!')
    else:
        category_q = Category.objects.get(title='자유')
        qs = Post.objects.filter(category=category_q)
    return render(request, 'blog/post_list.html',
                  {
                      "qs": qs,
                      "category_title": category_q,
                  })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    qs = Post.objects.filter(id=pk)

    return render(request, 'blog/post_detail.html', {
        "post": post,
        "category_title": post.category,
    })


def post_new(request):
    category = category_context(request)['category_title']
    print(category)
    if category:
        try:
            category_q = Category.objects.get(title=category)
        except ObjectDoesNotExist:
            return redirect('blog:post_list')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category_q
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {
        'form': form,
    })
