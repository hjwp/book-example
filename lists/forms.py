from django import forms

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


    def save(self, for_list):
        self.instance.list = for_list
        return super().save()


class ExistingListItemForm(forms.models.ModelForm):
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
