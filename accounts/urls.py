from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^(?P<email>.+@.+)/$', 'accounts.views.my_lists', name='my_lists'),
)
