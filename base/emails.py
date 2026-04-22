from django.core.mail import send_mail
from django.conf import settings

def send_account_activation_email(email, email_token):
    subject = 'Account Activation'
    message = f'Your account activation token is http://127.0.0.1:8000/accounts/activate/{email_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, [email])