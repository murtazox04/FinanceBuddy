from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin

from .models import User


@register(User)
class UserAdmin(ModelAdmin, BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('id', 'currency_type',)}),
    )
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'id')
