from django.core.exceptions import ValidationError
from django.test import TestCase

from lists.models import Item, List


class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list = List()
        list.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list
        second_item.save()

        saved_lists = List.objects.all()
        self.assertEqual(saved_lists.count(), 1)
        self.assertEqual(saved_lists[0], list)
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list)


    def test_get_absolute_url(self):
        list1 = List.objects.create()
        self.assertEqual(list1.get_absolute_url(), '/lists/%d/' % (list1.id,))


    def test_cannot_save_empty_list_items(self):
        list1 = List.objects.create()
        item = Item(list=list1, text='')
        with self.assertRaises(ValidationError):
            item.save()


    def test_cannot_save_duplicate_items(self):
        list1 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        with self.assertRaises(ValidationError):
            Item.objects.create(list=list1, text='bla')

