from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_registration_message_for_email(email):
    send_mail(
        subject="Потверждение регистрации",
        message="Пожалуйста, потвердите вашу регистрацию",
        from_email="fcdm2004@gmail.com",
        recipient_list=[email]
    )
