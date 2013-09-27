from django.conf.urls import patterns, include, url
from lists.views import HomePageView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^lists/', include('lists.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
