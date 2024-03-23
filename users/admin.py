from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    """Custom User Admin"""
    fieldsets = UserAdmin.fieldsets + (('Custom profile info', {'fields': ('avatar', 'bio', 'gender', 'birthday', 'language', 'currency', 'superhost',)}),)
