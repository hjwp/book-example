from django.conf.urls import url
from django.contrib.auth.views import logout
from accounts import views

urlpatterns = [
    url(r'^login$', views.persona_login, name='persona_login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]

