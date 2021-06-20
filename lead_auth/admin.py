from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LeadUser


class LeadUserAdmin(UserAdmin):
    list_filter = ('is_active',)
    list_display = ('email', 'phone_number', 'date_joined', 'last_login', 'is_active')
    search_fields = ('email', 'phone_number',)
    readonly_fields = ('date_joined', 'last_login')


# admin.site.unregister(LeadUser)
admin.site.register(LeadUser, LeadUserAdmin)
