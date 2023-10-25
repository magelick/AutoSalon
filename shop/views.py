from django.views.generic import TemplateView
from .forms import ContactForm
from .tasks import send_message_of_the_autosalon
from django.shortcuts import render, redirect
from django.contrib import messages


class ShopListView(TemplateView):
    """
    Класс представления Домашней старницы
    """
    template_name = 'shop/index.html'  # Шаблон
    context_object_name = 'shop'  # Данные на шаблоне


class AboutUsTemplateView(TemplateView):
    """
    Класс представления старницу О нас
    """
    template_name = 'shop/about.html'  # Шаблон


class ContactTemplateView(TemplateView):
    """
    Класс представления страницы Контакты
    """
    template_name = 'shop/contact.html'  # Шаблон
    context_object_name = 'contact'  # Данные на шаблоне

    # Метод, отбражающая форму на шаблоне
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()  # Расширяем словарь данных на шаблоне формой ContactForm
        return context

    # Метод, обрабатывающая данные из формы
    def post(self, request):
        form = ContactForm(request.POST)  # Берём заполненую форму

        if form.is_valid():  # Если данные валидны
            if request.user.is_authenticated:  # Если пользователь авторизован
                send_message_of_the_autosalon.delay(  # Отправляем в таску все данные
                    subject=form.cleaned_data['topic_of_the_question'],
                    message=form.cleaned_data['question'],
                    from_email=form.cleaned_data['email']
                )
            else:  # Если пользователь не авторизован
                messages.error(request, 'Вы не авторизованы!')  # Сообщение о том, что пользователь не авторизован
                return redirect('login/')  # Перенаправляем на страницу авторизации
        else:  # Если данные не валидны
            return render(  # Отображаем страницу заново
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )
