from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if not username:
            raise ValueError("Superuser must have a username.")
        return self._create_user(username=username, email=email, password=password, **extra_fields)


class User(AbstractUser):
    id = models.BigIntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    language_code = models.CharField(max_length=8, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class CurrencyType(models.TextChoices):
        UZS = "UZS", "Uzbekistan Sum"
        USD = "USD", "United States Dollar"
        RUB = "RUB", "Russian Ruble"
        EUR = "EUR", "Euro"

    currency_type = models.CharField(max_length=3, choices=CurrencyType.choices, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id']

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, First Name: {self.first_name}"

    def default_username(self):
        return f"FinanceBunny_{self.id}"


async def update_or_create_user(user_id, **kwargs):
    user, created = await User.objects.aupdate_or_create(id=user_id, defaults=kwargs)
    return user
