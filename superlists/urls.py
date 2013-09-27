from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    url(r'^$', list_views.HomePageView.as_view(), name='home'),
    url(r'^lists/', include(list_urls)),
]

