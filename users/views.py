from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegisterUsersForm, AuthenticationUsersForm


# Представление для регистрации новых пользователей
class SignUpView(CreateView):
    form_class = RegisterUsersForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Представление для входа пользователя
class CustomLoginView(LoginView):
    form_class = AuthenticationUsersForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('homepage')


# Представление для выхода пользователя
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
