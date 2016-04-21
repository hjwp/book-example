import json

from django.test import TestCase

from lists.models import List, Item


class ListAPITest(TestCase):
    base_url = '/api/lists/{}/'

    def test_get_returns_json_200(self):
        list_ = List.objects.create()
        response = self.client.get(self.base_url.format(list_.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')


    def test_GETting_items(self):
        list_ = List.objects.create()
        item1 = Item.objects.create(list=list_, text='item 1')
        item2 = Item.objects.create(list=list_, text='item 2')
        response = self.client.get(self.base_url.format(list_.id))
        self.assertEqual(
            json.loads(response.content.decode('utf8')),
            [
                {'id': item1.id, 'text': item1.text},
                {'id': item2.id, 'text': item2.text},
            ]
        )


    def test_POSTing_a_new_item(self):
        list_ = List.objects.create()
        response = self.client.post(
            self.base_url.format(list_.id),
            {'text': 'new item'},
        )
        self.assertEqual(response.status_code, 201)
        new_item = list_.item_set.get()
        self.assertEqual(new_item.text, 'new item')

