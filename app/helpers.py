from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def send_contact_mail(email,username,facebook,income,message):
    subject = 'Django Send Mail'
    from_email = settings.EMAIL_HOST
    recipient_list = [email]
    html_message = render_to_string("mail.html",context={'email':email,'username':username,'facebook':facebook,'income':income,'message':message,})
    message = EmailMessage(subject, html_message,from_email, recipient_list)
    message.content_subtype = 'html'
    message.send()
    return True

