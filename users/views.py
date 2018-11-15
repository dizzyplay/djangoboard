from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError

from .models import Profile
from .tasks import send_email_check
from .forms import JoinForm

User = get_user_model()


def email_checker(request):
    get_hash = request.GET.get('hash', False)
    user_id = request.GET.get('id', False)

    try:
        user = User.objects.get(id=user_id)
        if user.profile.status is not True and user_id and get_hash:
            if check_password(user.email, get_hash):
                profile = Profile.objects.get(user=user.id)
                profile.status = True
                profile.save()
                valid_message = '이메일 인증이 완료되어 계정이 활성화 되었습니다.'
        else:
            valid_message = '잘못된 접근입니다.'
    except:
        valid_message = '잘못된 접근입니다'


    return render(request, 'users/email_checker.html', {
        'valid_message': valid_message,
    })


def sign_up(request):
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.nickname = form.cleaned_data.get('nickname')
            user.save()
            print(user.id)
            post_dict={
                'user_email': user.email,
                'username' : user.username,
                'user_id' : user.id,
                'hash':make_password(user.email)
            }
            send_email_check(post_dict)
            print(form.cleaned_data.get('nickname'))

            return render(request, 'users/confirm_your_info.html', {
                'email': user.email,
            })
        else:
            return render(request, 'users/reject_your_info.html', {
                'form': form,
            })
    return redirect('blog:post_list')


# def sign_up(request):
#     if request.method == 'POST':
#         email = request.POST.get('email', None)
#         id = request.POST.get('username', None)
#         nickname = request.POST.get('nickname', None)
#         password = request.POST.get('password2', None)
#
#         check_email = Profile.objects.filter(email=email)
#         check_nickname = Profile.objects.filter(nickname=nickname)
#
#         if len(check_email) + len(check_nickname) == 0:
#             try:
#                 password = make_password(password)
#                 user = User.objects.create(username=id, password=password)
#                 profile = Profile.objects.create(user=user, nickname=nickname, email=email, status=False)
#                 post_dict={
#                     'user_email': profile.email,
#                     'username' : user.username,
#                     'user_id' : user.id,
#                     'hash':make_password(profile.email)
#                 }
#                 send_email_check(post_dict)
#             except IntegrityError:
#                 return render(request, 'users/reject_your_info.html', {
#                     'reject': 'ID가 이미 존재합니다.'
#                 })
#         else:
#             return render(request, 'users/reject_your_info.html', {
#                 'reject': 'email 또는 닉네임이 존재합니다.'
#             })
#         print(profile.email)
#         return render(request, 'users/confirm_your_info.html', {
#             'email': email,
#         })
#     return render('blog:post_list')


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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None and user.profile.status is True:
            if user.profile.status is False:
                messages.error(request, '계정활성화가 필요합니다.')
            else:
                login(request, user)
                messages.success(request, '로그인성공')
            return redirect('blog:post_list')
        else:
            messages.error(request, '아이디/비밀번호가 잘못 되었습니다.')
    return redirect('blog:post_list')
