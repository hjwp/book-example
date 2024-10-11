from django.contrib import auth, messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import Token


def send_login_email(request):
    email = request.POST["email"]
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse("login") + "?token=" + str(token.uid),
    )
    message_body = f"Use this link to log in:\n\n{url}"
    send_mail(
        "Your login link for Superlists",
        message_body,
        "noreply@superlists",
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in.",
    )
    return redirect("/")


def login(request):
    # TODO: call authenticate(),
    auth.authenticate("bang!")
    # then auth.login() with the user if we get one,
    # or messages.error() if we get None.
    return redirect("/")
