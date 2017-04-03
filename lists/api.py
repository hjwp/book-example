import json
from django.http import HttpResponse
from lists.models import List, Item
from lists.forms import (
    ExistingListItemForm,
    EMPTY_ITEM_ERROR,
)
from rest_framework import routers, serializers, viewsets


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'text')


class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, source='item_set')

    class Meta:
        model = List
        fields = ('id', 'items',)



def list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(
                json.dumps({'error': form.errors['text'][0]}),
                content_type='application/json',
                status=400
            )
    item_dicts = [
        {'id': item.id, 'text': item.text}
        for item in list_.item_set.all()
    ]
    return HttpResponse(
        json.dumps(item_dicts),
        content_type='application/json'
    )


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


router = routers.SimpleRouter()
router.register(r'lists', ListViewSet)
