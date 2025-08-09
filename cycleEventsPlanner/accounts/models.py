from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

from accounts.managers import AccountManager
from common.validators import validate_image_size


# Create your models here.
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'

    objects = AccountManager()


class Profile(models.Model):
    user = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    nickname = models.CharField(
        max_length=50,
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='upload/',
        validators=[validate_image_size, ],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nickname

    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}"
