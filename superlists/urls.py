from django.urls import path, include
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    path('', list_views.home_page, name='home'),
    path('lists/', include(list_urls)),
]
