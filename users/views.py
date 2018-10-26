from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib import messages
from django.shortcuts import redirect

from .models import Profile

User = get_user_model()


def user_profile(request):
    user_obj = User.objects.get(username=request.user)
    user_profile_obj = Profile.objects.get(user=user_obj)
    print(user_obj)
    print(user_profile_obj)
    return render(request, 'users/profile.html',{
        'user_obj': user_obj,
        'user_profile': user_profile_obj,
    })


def logout_view(request):
    logout(request)
    return redirect('blog:post_list')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, '로그인성공')
        return redirect('blog:post_list')
    else:
        messages.error(request, '아이디/비밀번호가 잘못 되었습니다.')
    return redirect('blog:post_list')
