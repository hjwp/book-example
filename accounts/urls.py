from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login$', 'accounts.views.persona_login', name='persona_login'),
)
