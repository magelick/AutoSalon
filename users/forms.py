from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class AuthenticationUsersForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.EmailInput
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput
    )