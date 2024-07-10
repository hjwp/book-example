from django.core.mail import send_mail
from django.shortcuts import redirect


def send_login_email(request):
    send_mail("subject", "body", "from_email", ["to email"])
    return redirect("/")
