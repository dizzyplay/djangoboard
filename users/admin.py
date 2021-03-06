from django.contrib import admin
from .models import Profile


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('nickname', 'user', 'status')
    ordering = ['-id']
