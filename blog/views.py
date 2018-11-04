from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Category
from .forms import PostForm
from .context_processors import category_context
from .paginator import CustomPaginator, page_range_check


def post_list(request):
    category = category_context(request)['category_title']
    page = int(request.GET.get('page', 1))

    if category:
        try:
            category_q = Category.objects.get(title=category)
            qs = Post.objects.filter(category=category_q)
            p = CustomPaginator(qs, 3)
            qs = p.get_page(page)
            page_start, page_end = page_range_check(page, p.num_pages)
        except ObjectDoesNotExist:
            print('object does not exist!!!')
    else:
        category_q = Category.objects.get(title='자유')
        qs = Post.objects.filter(category=category_q)
    return render(request, 'blog/post_list.html',
                  {
                      "qs": qs,
                      "pages": p,
                      "prange": p.custom_page_range(int(page_start), int(page_end)),
                      "category_title": category_q,
                  })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    page = int(request.GET.get('page', 1))
    category = request.GET.get('category','자유')
    if category:
        category = Category.objects.get(title=category)
        qs = Post.objects.filter(category=category)
        p = CustomPaginator(qs, 3)
        qs = p.get_page(page)
        page_start, page_end = page_range_check(page, p.num_pages)

    return render(request, 'blog/post_detail.html', {
        "post": post,
        "category_title": post.category,
        "pages": p,
        "prange": p.custom_page_range(int(page_start), int(page_end)),
        "qs": qs,
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
