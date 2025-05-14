from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR,
    EMPTY_ITEM_ERROR,
    ExistingListItemForm,
    ItemForm,
)
from lists.models import Item, List


class ItemFormTest(TestCase):
    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={"text": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], [EMPTY_ITEM_ERROR])

    def test_save_new_list(self):
        form = ItemForm(data={"text": "do me"})
        self.assertTrue(form.is_valid())
        new_list = form.save_new_list()
        self.assertEqual(new_list.item_set.get().text, "do me")


class ExistingListItemFormTest(TestCase):
    def test_form_validation_for_blank_items(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={"text": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], [EMPTY_ITEM_ERROR])

    def test_form_validation_for_duplicate_items(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text="no twins!")
        form = ExistingListItemForm(for_list=list_, data={"text": "no twins!"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], [DUPLICATE_ITEM_ERROR])

    def test_save_item(self):
        mylist = List.objects.create()
        form = ExistingListItemForm(for_list=mylist, data={"text": "hi"})
        self.assertTrue(form.is_valid())
        form.save_item()
        self.assertEqual(mylist.item_set.get().text, "hi")
