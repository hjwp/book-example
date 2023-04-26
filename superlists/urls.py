from django.urls import path
from lists.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
]
