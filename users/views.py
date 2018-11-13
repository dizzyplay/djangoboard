from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

from .models import Profile

User = get_user_model()


def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        id = request.POST.get('username', None)
        nickname = request.POST.get('nickname', None)
        password = request.POST.get('password2', None)

        check_email = Profile.objects.filter(email=email)
        check_nickname = Profile.objects.filter(nickname=nickname)

        if len(check_email) == 0 and len(check_nickname) == 0:
            try:
                password = make_password(password)
                user = User.objects.create(username=id, password=password)
                profile = Profile.objects.create(user=user, nickname=nickname, email=email)

            except IntegrityError:
                return render(request, 'users/reject_your_info.html', {
                    'reject': 'ID가 이미 존재합니다.'
                })
        else:
            return render(request, 'users/reject_your_info.html', {
                'reject': 'email 또는 닉네임이 존재합니다.'
            })

        return render(request, 'users/confirm_your_info.html', {
            'info': profile
        })

    return render('blog:post_list')


def user_profile(request):
    user_obj = User.objects.get(username=request.user)
    user_profile_obj = Profile.objects.get(user=user_obj)
    print(user_obj)
    print(user_profile_obj)
    return render(request, 'users/profile.html', {
        'user_obj': user_obj,
        'user_profile': user_profile_obj,
    })


@login_required
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
