from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/the-only-list-in-the-world/$', 'lists.views.view_list',
        name='view_list'
    ),
    url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    # url(r'^admin/', include(admin.site.urls)),
)
