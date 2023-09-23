from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import RegisterUsersForm, AuthenticationUsersForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Представление для регистрации новых пользователей
class SignUpView(CreateView):
    form_class = RegisterUsersForm
    template_name = 'users/sign_up.html'

    def post(self, request):
        form = RegisterUsersForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        messages.error(request=request, message="Что-то не верно введено")
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form}
        )


# Представление для входа пользователя
class CustomLoginView(LoginView):
    form_class = AuthenticationUsersForm
    template_name = 'users/login.html'

    def get(self, request):
        form = AuthenticationUsersForm(request.GET)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request=request,
                username=username,
                password=password
            )
            if user:
                login(request, user)
                return redirect('homepage')
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form}
        )