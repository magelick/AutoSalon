from celery import shared_task
from django.core.mail import send_mail


# Таска, отправляющая письмо на почту автосалона
@shared_task()
def send_message_of_the_autosalon(subject, message, from_email):
    send_mail(
        subject=subject,  # Тема сообщения
        message=message,  # Само сообщение
        from_email=from_email,  # От кого было отправленно сообщение
        recipient_list=['fcdm2004@gmail.com']  # Список получателей сообщение
    )
