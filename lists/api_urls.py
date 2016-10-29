from django.conf.urls import url
from lists import api

urlpatterns = [
    url(r'^lists/(\d+)/$', api.list, name='api_list'),
]

