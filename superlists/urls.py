from django.urls import path
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
]
