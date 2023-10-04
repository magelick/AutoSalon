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
    class Meta:
        model = None
        fields = [
            'username',
            'password'
        ]
