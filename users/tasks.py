from celery import shared_task
from django.core.mail import send_mail


# Таска, отправляющая сообщение о потверждении регистрации пользователя
@shared_task()
def send_registration_message_for_email(email):
    send_mail(
        subject="Потверждение регистрации",  # Тема сообщения
        message="Пожалуйста, потвердите вашу регистрацию на нашем сайте",  # Само сообщение
        from_email="fcdm2004@gmail.com",  # От кого это сообщение
        recipient_list=[email]  # Список почт получателей зи формы ContactForm
    )
