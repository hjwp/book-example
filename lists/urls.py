from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/share$', views.share_list, name='share_list'),
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]

