from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin


@admin.register(UserProfile)
class BloggerAdmin(admin.ModelAdmin):
    fieldset= ['birthday','gender','mobile']
