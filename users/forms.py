from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterUsersForm(UserCreationForm):
    """
    Форма регистраци пользователя
    """
    class Meta:
        model = User  # Берём поля из стандартной модели Пользователя
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class AuthenticationUsersForm(AuthenticationForm):
    """
    Форма авторизации пользователя
    """
    class Meta:
        model = None  # Используем не модель Пользователя, а просто поля Имени пользователя и его пароль
        fields = [
            'username',
            'password'
        ]
