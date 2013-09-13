from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR,
    ExistingListItemForm, ItemForm
)
from lists.models import Item, List


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())


    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])



class ExistingListItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ExistingListItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())


    def test_form_validation_for_blank_items(self):
        listey = List.objects.create()
        form = ExistingListItemForm(data={'list': listey.id, 'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])


    def test_form_validation_for_duplicate_items(self):
        listey = List.objects.create()
        Item.objects.create(list=listey, text='no twins!')
        form = ExistingListItemForm(data={'list': listey.id, 'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])
        self.assertFalse(form.non_field_errors())
