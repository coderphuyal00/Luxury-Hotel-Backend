from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

# full_message = f"Question from {name} <{email}>:\n\n{question} for {department} deparment."
# send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])