from django.test import TestCase

from lists.forms import ItemForm


class ItemFormTest(TestCase):
    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control form-control-lg"', form.as_p())
