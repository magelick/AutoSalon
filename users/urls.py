from django.urls import path
from .views import RegisterUsersView, LoginUsersView

urlpatterns = [
    path('register/', RegisterUsersView.as_view(), name='register'),
    path('login/', LoginUsersView.as_view(), name='login'),
]
