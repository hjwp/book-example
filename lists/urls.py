from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.NewListView.as_view(), name='new_list'),
    url(r'^(\d+)/$', views.ViewAndAddToList.as_view(), name='view_list'),
]

