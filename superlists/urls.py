from django.urls import path, include
from lists import views as list_views

urlpatterns = [
    path("", list_views.home_page, name="home"),
    path("lists/", include("lists.urls")),
]
