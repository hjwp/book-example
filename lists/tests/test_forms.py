from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR,
    ExistingListItemForm, ItemForm
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


    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'do me'})
        new_item = form.save(for_list=list_, user=AnonymousUser())
        self.assertEqual(new_item, Item.objects.all()[0])
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)


    def test_form_save_sets_owner_if_real_user(self):
        list_ = List.objects.create()
        user = User.objects.create()
        form = ItemForm(data={'text': 'save me'})
        new_item = form.save(for_list=list_, user=user)
        self.assertEqual(new_item.list.owner, user)


    def test_form_save_ignores_anon_user(self):
        list_ = List.objects.create()
        user = AnonymousUser()
        form = ItemForm(data={'text': 'save me'})
        new_item = form.save(for_list=list_, user=user)
        self.assertEqual(new_item.list.owner, None)



class ExistingListItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        listey = List.objects.create()
        form = ExistingListItemForm(for_list=listey)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())


    def test_form_validation_for_blank_items(self):
        listey = List.objects.create()
        form = ExistingListItemForm(for_list=listey, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_LIST_ERROR])


    def test_form_validation_for_duplicate_items(self):
        listey = List.objects.create()
        Item.objects.create(list=listey, text='no twins!')
        form = ExistingListItemForm(for_list=listey, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])


    def test_form_save(self):
        listey = List.objects.create()
        form = ExistingListItemForm(for_list=listey, data={'text': 'hi'})
        new_item = form.save()
        self.assertEqual(new_item, Item.objects.all()[0])

