from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
