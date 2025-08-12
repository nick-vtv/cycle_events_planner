from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import Profile

UserModel = get_user_model()


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', ]


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ['email', ]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'age', 'profile_picture', ]
        labels = {
            'nickname': 'Nickname',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'profile_picture': 'Upload a Profile Picture (optional)',
        }

        widgets = {
            'nickname': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your nickname:'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your first name (optional):'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your last name (optional):'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter your age (optional):'
                }
            ),
            'profile_picture': forms.FileInput(),
        }
