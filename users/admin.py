from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# these you created in forms.py
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()  # recommended way of doing this


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

    title = "Test title"


admin.site.register(CustomUser, CustomUserAdmin)