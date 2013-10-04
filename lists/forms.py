from django import forms

from lists.models import Item

DUPLICATE_ITEM_ERROR = "You've already got this in your list"
EMPTY_LIST_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].error_messages['required'] = EMPTY_LIST_ERROR


    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(
                attrs={'placeholder': 'Enter a to-do item'}
            ),
        }



class ExistingListItemForm(ItemForm):

    def __init__(self, *args, **kwargs):
        self.list = kwargs.pop('list', None)
        super().__init__(*args, **kwargs)

    class Meta(ItemForm.Meta):
        fields = ('text',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.list = list
        if commit:
            instance.save()
        return instance

    def validate_unique(self):
        super().validate_unique()
        if self.non_field_errors():
            self._update_errors({'text': [DUPLICATE_ITEM_ERROR]})
            del self.errors['__all__']
