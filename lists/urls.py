from django.conf.urls import patterns, url
from lists.views import NewListView, ViewAndAddToList

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', ViewAndAddToList.as_view(), name='view_list'),
    url(r'^new$', NewListView.as_view(), name='new_list'),
)
