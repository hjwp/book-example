from django.contrib.auth.models import AnonymousUser
from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item

DUPLICATE_ITEM_ERROR = "You've already got this in your list"
EMPTY_LIST_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].error_messages['required'] = EMPTY_LIST_ERROR


    def save(self, for_list, user):
        self.instance.list = for_list
        if not isinstance(user, AnonymousUser):
            self.instance.list.owner = user
            self.instance.list.save()
        return super().save()


class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list


    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError:
            self._update_errors({'text': [DUPLICATE_ITEM_ERROR]})


    def save(self):
        return super(forms.models.ModelForm, self).save()

