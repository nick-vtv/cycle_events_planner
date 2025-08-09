from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import Profile

UserModel = get_user_model()


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', ]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
