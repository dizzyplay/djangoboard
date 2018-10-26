from django.shortcuts import render
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


def user_profile(request):
    user_obj = User.objects.get(username=request.user)
    user_profile_obj = Profile.objects.get(user=user_obj)
    print(user_obj)
    print(user_profile_obj)
    return render(request, 'users/profile.html',{
        'user': user_obj,
        'user_profile': user_profile_obj,
    })


