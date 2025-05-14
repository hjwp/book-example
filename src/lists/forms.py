from django import forms

from lists.models import Item, List

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


class _ItemForm(forms.Form):
    text = forms.CharField(
        error_messages={"required": EMPTY_ITEM_ERROR},
        required=True,
    )


class ItemForm(_ItemForm):
    def save_new_list(self):
        new_list = List.objects.create()
        Item.objects.create(
            list=new_list,
            text=self.cleaned_data["text"],
        )
        return new_list


class ExistingListItemForm(_ItemForm):
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._for_list = for_list

    def clean_text(self):
        text = self.cleaned_data["text"]
        if self._for_list.item_set.filter(text=text).exists():
            raise forms.ValidationError(DUPLICATE_ITEM_ERROR)
        return text or ""

    def save_item(self):
        Item.objects.create(
            list=self._for_list,
            text=self.cleaned_data["text"],
        )
