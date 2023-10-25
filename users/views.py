from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import RegisterUsersForm, AuthenticationUsersForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .tasks import send_registration_message_for_email


class RegisterUsersView(CreateView):
    """ Представление для регистрации новых пользователей"""
    form_class = RegisterUsersForm   # Форма для класса
    template_name = 'users/register.html'  # Шаблон

    # Метод для обработки данных из формы
    def post(self, request, *args, **kwargs):
        form = RegisterUsersForm(request.POST)  # Берём заполненую форму

        if form.is_valid():  # Песли данные валидины
            form.save()  # Сохраняем их
            send_registration_message_for_email.delay(email=form.cleaned_data['email'])  # И отправляем в таску для
            # потверждения регистрации
            return redirect('login')  # И перенапрвляем на страницу с авторизацией
        else:  # Если данные не валидны
            return render(  # Заново отрисовываем страницу
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )


class LoginUsersView(LoginView):
    """ Представление для входа пользователей"""
    form_class = AuthenticationUsersForm  #
    template_name = 'users/login.html'  #

    # Метод для обработки данных из формы
    def post(self, request, *args, **kwargs):
        form = AuthenticationUsersForm(request.GET)  # Берём заполеную форму

        username = self.request.POST.get('username')  # Достаём имя пользователя
        password = self.request.POST.get('password')  # Достаём пароль

        user = authenticate(  # Поверяем, есть ли пользователь с таким именем и паролем
            request=request,
            username=username,
            password=password
        )
        if user:  # Если пользователь существует
            login(request, user)  # ЛОгиним его
            return redirect('homepage')  # И перенаправляем его на домашнюю страницу
        else:  # Если пользователя нет
            return render(  # Отрисовываем страницу заново
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )
