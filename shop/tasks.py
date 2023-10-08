from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_message_of_the_autosalon(subject, message, from_email):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=['fcdm2004@gmail.com']
    )
