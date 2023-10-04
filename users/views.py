from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import RegisterUsersForm, AuthenticationUsersForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .tasks import send_registration_message_for_email


class RegisterUsersView(CreateView):
    """ Представление для регистрации новых пользователей"""
    form_class = RegisterUsersForm
    template_name = 'users/register.html'

    def post(self, request, *args, **kwargs):
        form = RegisterUsersForm(request.POST)

        if form.is_valid():
            form.save()
            send_registration_message_for_email.delay(email=form.cleaned_data['email'])
            return redirect('login')
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )


class LoginUsersView(LoginView):
    """ Представление для входа пользователей"""
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
