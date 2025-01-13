from django.contrib.admin import register
from unfold.admin import ModelAdmin

from .models import Expense, Income, Goal, Notification, ExpenseCategory


@register(ExpenseCategory)
class ExpenseCategoryAdmin(ModelAdmin):
    list_display = ('user', 'name', 'parent', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    autocomplete_fields = ('parent', 'user')


@register(Expense)
class ExpenseAdmin(ModelAdmin):
    list_display = ('user', 'category', 'amount', 'created_at')
    list_filter = ('created_at', 'category')
    search_fields = ('user__username', 'category__name',)
    autocomplete_fields = ('category',)


@register(Income)
class IncomeAdmin(ModelAdmin):
    list_display = ('user', 'source', 'amount', 'created_at')
    search_fields = ('user__username', 'source')
    autocomplete_fields = ('user',)


@register(Goal)
class GoalAdmin(ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'saved_amount', 'deadline', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('user__username', 'name')
    autocomplete_fields = ('user',)


@register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('user__username', 'message')
    autocomplete_fields = ('user',)
