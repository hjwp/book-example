from django.conf.urls import include, url
from accounts import urls as accounts_urls
from lists import views as list_views
from lists import urls as list_urls
from lists import api_urls

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^api/', include(api_urls)),
]

