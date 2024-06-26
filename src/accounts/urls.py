from django.urls import path

from accounts import views

urlpatterns = [
    path("send_email", views.send_login_email, name="send_login_email"),
]
