from users.forms import LoginForm, JoinForm
from .models import Category


def blog_custom_context(request):
    category_title = request.GET.get('category', None)
    login_form = LoginForm()
    join_form = JoinForm()
    category_list = Category.objects.all()
    if category_title is None:
        category_title = Category.objects.first()

    return {
        "category_title": category_title,
        "login_form": login_form,
        "join_form": join_form,
        "category_list": category_list,
    }
