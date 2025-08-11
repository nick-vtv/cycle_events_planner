from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import AccountCreationForm
from accounts.models import Profile

UserModel = get_user_model()

# Register your models here.
@admin.register(UserModel)
class AccountAdmin(UserAdmin):
    form = AccountCreationForm

    list_display = ('email', 'is_active', 'is_staff',)

    ordering = ('email',)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
