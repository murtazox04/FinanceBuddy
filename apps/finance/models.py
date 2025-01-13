from django.db import models

from apps.users.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExpenseCategory(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='personal_categories')
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def is_global(self):
        return self.user is None


class Expense(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        category = self.category.name if self.category else self.user_category.name
        return f"{category} - {self.amount} ({self.user.username})"


class Income(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    source = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.amount} ({self.user.username})"


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.target_amount} ({self.user.username})"


class Notification(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
