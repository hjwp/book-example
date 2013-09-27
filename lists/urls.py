from django.conf.urls import patterns, url
from lists.views import NewListView

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^new$', NewListView.as_view(), name='new_list'),
)
