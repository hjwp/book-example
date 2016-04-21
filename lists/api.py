import json
from django.http import HttpResponse
from lists.models import List


def list(request, list_id):
    list_ = List.objects.get(id=list_id)
    item_dicts = [
        {'id': item.id, 'text': item.text}
        for item in list_.item_set.all()
    ]
    return HttpResponse(
        json.dumps(item_dicts),
        content_type='application/json'
    )

