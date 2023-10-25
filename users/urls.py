from django.urls import path
from .views import RegisterUsersView, LoginUsersView

# Пути к страницам регистарции и авторизации пользователя
urlpatterns = [
    path('register/', RegisterUsersView.as_view(), name='register'),  # Ссылка на страницу регистрации
    path('login/', LoginUsersView.as_view(), name='login'),  # Сслыка на страницу авторизации
]
