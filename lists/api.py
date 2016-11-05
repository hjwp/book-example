from django.core.exceptions import ValidationError
from django.conf.urls import url
from lists.models import List, Item
from rest_framework import serializers, generics
from lists.forms import EMPTY_ITEM_ERROR, DUPLICATE_ITEM_ERROR


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
        item = Item(list=list_, text=serializer.validated_data.get('text'))
        try:
            item.full_clean()
            item.save()
        except ValidationError as e:
            if 'text' in e.message_dict:
                error = EMPTY_ITEM_ERROR
            if '__all__' in e.message_dict:
                error = DUPLICATE_ITEM_ERROR
            raise serializers.ValidationError({'error': error})







urlpatterns = [
    url(r'^lists/(?P<id>\d+)/$', ListAPIView.as_view(), name='api_list'),
]


