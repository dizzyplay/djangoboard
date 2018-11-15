from users.forms import LoginForm, JoinForm


def blog_custom_context(request):
    category_title = request.GET.get('category', None)
    login_form = LoginForm()
    join_form = JoinForm()
    if category_title is None:
        category_title = '자유'

    return {
        "category_title": category_title,
        "login_form": login_form,
        "join_form": join_form,
    }
