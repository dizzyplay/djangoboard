from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError

from .models import Profile

User = get_user_model()


def email_checker(request):
    get_hash = request.GET.get('hash', None)
    user_id = request.GET.get('user_id', None)
    user = User.objects.get(id=user_id)

    if user.profile.status is not True:
        if check_password(user.profile.email, get_hash):
            profile = Profile.objects.get(user=user.id)
            profile.status = True
            profile.save()
            valid_message = '이메일 인증이 완료되어 계정이 활성화 되었습니다.'
    else:
        valid_message = '잘못된 접근입니다.'
    return render(request, 'users/email_checker.html', {
        'valid_message': valid_message,
    })


def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        id = request.POST.get('username', None)
        nickname = request.POST.get('nickname', None)
        password = request.POST.get('password2', None)

        check_email = Profile.objects.filter(email=email)
        check_nickname = Profile.objects.filter(nickname=nickname)

        if len(check_email) + len(check_nickname) == 0:
            try:
                password = make_password(password)
                hash_value = make_password(email)
                user = User.objects.create(username=id, password=password)
                profile = Profile.objects.create(user=user, nickname=nickname, email=email, hash=hash_value,
                                                 status=False)
            except IntegrityError:
                return render(request, 'users/reject_your_info.html', {
                    'reject': 'ID가 이미 존재합니다.'
                })
        else:
            return render(request, 'users/reject_your_info.html', {
                'reject': 'email 또는 닉네임이 존재합니다.'
            })
        print(profile.email)
        return render(request, 'users/confirm_your_info.html', {
            'info': profile,
            'user': user,
            'hashed_value': make_password(profile.email),
        })
    return render('blog:post_list')


@login_required
def user_profile(request):
    user_obj = User.objects.get(username=request.user)
    user_profile_obj = Profile.objects.get(user=user_obj)
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
    if user is not None and user.profile.status is True:
        login(request, user)
        messages.success(request, '로그인성공')
        return redirect('blog:post_list')
    elif user.profile.status is False:
        messages.error(request, '계정 활성화가 필요합니다.')
    else:
        messages.error(request, '아이디/비밀번호가 잘못 되었습니다.')
    return redirect('blog:post_list')
