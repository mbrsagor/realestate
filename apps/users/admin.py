from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['pkid', 'id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser',
                    'is_active']
    list_filter = ['email', 'username', 'first_name', 'last_name']
    list_display_links = ['id', 'username']
    search_fields = ['email', 'username', 'first_name']
    # fieldsets = (
    #     (
    #         _('Login Credentials'),
    #         {
    #             'fields': ('email', 'password',)
    #         }
    #     ),
    #     (
    #         _('Personal Information'),
    #         {'fields': ('username', 'first_name', 'last_name')}
    #     ),
    #     (
    #         _('Permissions and Groups'),
    #         {'fields': ('username', 'is_active', 'is_superuser', 'is_active', 'groups', 'use_permissions')}
    #     ),
    #     (
    #         _('Important Dates'),
    #         {'fields': ('last_login', 'date_joined')}
    #     )
    # )


admin.site.register(User, UserAdmin)
