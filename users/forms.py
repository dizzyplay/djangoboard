from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import mark_safe

User = get_user_model()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'id': 'inputId',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control form-control-sm',
                'id': 'inputPassword'
            })
        }
        labels = {
            'username': '사용자ID'
        }
        help_texts = {
            'username': '',
        }


class JoinForm(UserCreationForm):
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(attrs={
            'class':'form-control form-control-sm',
        })
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={
            'class':'form-control form-control-sm',
        })
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={
            'class':'form-control form-control-sm',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'id': 'joinId'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'id': 'joinEmail'
            }),
        }
        labels = {
            'username':mark_safe('ID <span class="badge badge-dark">로그인시 사용될 아이디</span></label> '),
            'email':mark_safe('Email <span class="badge badge-dark">인증메일이 발송됩니다</span></label> ')
        }

