def category_context(request):
    category_title = request.GET.get('category')
    if category_title is None:
        category_title = ''

    return {
        "category_title": category_title
    }