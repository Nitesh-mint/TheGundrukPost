from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


CustomUser = get_user_model() # referring to the User model created in models.py

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]


admin.site.register(CustomUser)