from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegisterUsersForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if not username:
            raise ValidationError("Введите имя пользователя")
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email:
            raise ValidationError("Введите адрес электронной почты")
        else:
            return email

    def clean_password(self):
        password1 = self.cleaned_data.get("password1")

        if not password1:
            raise ValidationError("Введите пароль")
        else:
            return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password2:
            raise ValidationError("Введите потверждение пароля")
        if password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2


class AuthenticationUsersForm(AuthenticationForm):
    class Meta:
        model = None
        fields = [
            'username',
            'password'
        ]

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not username or not password:
            raise ValidationError("Введите имя или пароль")
        else:
            return username, password
