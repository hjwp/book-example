from django.conf.urls import url
from lists.models import List, Item
from rest_framework import serializers, generics


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'text')


class ListAPIView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        list_ = List.objects.get(id=self.kwargs['id'])
        return list_.item_set.all()

    def perform_create(self, serializer):
        list_ = List.objects.get(id=self.kwargs['id'])
        Item.objects.create(list=list_, text=serializer.validated_data['text'])



urlpatterns = [
    url(r'^lists/(?P<id>\d+)/$', ListAPIView.as_view(), name='api_list'),
]


