
def category_context(request):
    category_title = request.GET.get('category',None)
    if category_title is None:
        category_title = '자유'

    return {
        "category_title": category_title
    }