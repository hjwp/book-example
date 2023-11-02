from django import forms

from lists.models import Item


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ("text",)
        widgets = {
            "text": forms.widgets.TextInput(
                attrs={
                    "placeholder": "Enter a to-do item",
                    "class": "form-control form-control-lg",
                }
            ),
        }
        error_messages = {"text": {"required": "You can't have an empty list item"}}
