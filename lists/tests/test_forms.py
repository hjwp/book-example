import unittest
from unittest.mock import patch, Mock
from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR,
    ExistingListItemForm, ItemForm, NewListForm
)
from lists.models import Item, List


class ItemFormTest(TestCase):

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())


    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])



@patch('lists.forms.List')
@patch('lists.forms.Item')
class NewListFormTest(unittest.TestCase):

    def test_is_an_ItemForm(self, mockItem, mockList):
        self.assertIsInstance(NewListForm(), ItemForm)


    def test_save_creates_new_list_and_item_from_cleaned_data(
        self, mockItem, mockList
    ):
        mock_item = mockItem.return_value
        mock_list = mockList.return_value
        user = Mock()
        form = NewListForm()
        form.cleaned_data = {'text': 'new item text'}

        def check_item_text_and_list():
            self.assertEqual(mock_item.text, 'new item text')
            self.assertEqual(mock_item.list, mock_list)
            self.assertTrue(mock_list.save.called)
        mock_item.save.side_effect = check_item_text_and_list

        form.save(owner=user)

        self.assertTrue(mock_item.save.called)


    def test_save_saves_owner_if_authenticated(self, mockItem, mockList):
        mock_list = mockList.return_value
        mock_list.owner = None
        user = Mock(is_authenticated=lambda: True)
        form = NewListForm()
        form.cleaned_data = {'text': 'new item text'}

        form.save(owner=user)

        self.assertEqual(mock_list.owner, user)


    def test_does_not_save_owner_if_not_authenticated(self, mockItem, mockList):
        mock_list = mockList.return_value
        mock_list.owner = None
        user = Mock(is_authenticated=lambda: False)
        form = NewListForm()
        form.cleaned_data = {'text': 'new item text'}

        form.save(owner=user)

        self.assertEqual(mock_list.owner, None)


    def test_save_returns_new_list_object(self, mockItem, mockList):
        mock_list = mockList.return_value
        user = Mock(is_authenticated=lambda: True)
        form = NewListForm()
        form.cleaned_data = {'text': 'new item text'}

        response = form.save(owner=user)

        self.assertEqual(response, mock_list)



class ExistingListItemFormTest(TestCase):

    def test_is_an_ItemForm(self):
        self.assertIsInstance(ExistingListItemForm(for_list=List()), ItemForm)

    def test_form_validation_for_duplicate_items(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='no twins!')
        form = ExistingListItemForm(for_list=list_, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])


    def test_form_save(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': 'hi'})
        new_item = form.save()
        self.assertEqual(new_item, Item.objects.all()[0])

