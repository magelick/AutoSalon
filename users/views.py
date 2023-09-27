from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import RegisterUsersForm, AuthenticationUsersForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Представление для регистрации новых пользователей
class SignUpView(CreateView):
    form_class = RegisterUsersForm
    template_name = 'users/sign_up.html'

    def post(self, request, *args, **kwargs):
        form = RegisterUsersForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )


# Представление для входа пользователя
class CustomLoginView(LoginView):
    form_class = AuthenticationUsersForm
    template_name = 'users/login.html'

    def post(self, request, *args, **kwargs):
        form = AuthenticationUsersForm(request.GET)

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = authenticate(
            request=request,
            username=username,
            password=password
        )
        if user:
            login(request, user)
            return redirect('homepage')
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )
