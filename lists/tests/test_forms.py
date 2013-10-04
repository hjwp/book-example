from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR,
    ExistingListItemForm, ItemForm
)
from lists.models import Item, List

from django.http import QueryDict
from urllib.parse import urlencode


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
        listey = List()
        form = ExistingListItemForm(list=listey)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())


    def test_form_validation_for_blank_items(self):
        listey = List.objects.create()
        form = ExistingListItemForm(list=listey, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])


    def test_form_validation_for_duplicate_items(self):
        listey = List.objects.create()
        Item.objects.create(list=listey, text='no twins!')
        form = ExistingListItemForm(list=listey, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])
        self.assertFalse(form.non_field_errors())


    def test_form_handles_querydicts(self):
        listey = List()
        ExistingListItemForm(
            list=listey,
            data=QueryDict(urlencode({'text': 'hello'}))
        ) # should not raise
