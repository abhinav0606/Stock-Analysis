from django.conf import settings
from django.core.mail import send_mail
def send(name,email):
    subject="Welcome To Stock-o-lysis"
    message = f'Hi {name}, thank you for registering in Stock-o-lysis.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)