from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_registration_message_for_email(email):
    subject = "Потвердждение регистрации"
    message = "Пожалуйста, потвердите вашу регистрацию"
    from_email = "autosalon№1@gmail.com"
    recipient_list = [email]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )
