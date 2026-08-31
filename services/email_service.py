from django.conf import settings
from django.core.mail import send_mail

def send_email(subject, message, recipient):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])