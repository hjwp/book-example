from django import forms

from lists.models import Item


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ("text",)
        widgets = {
            "text": forms.widgets.TextInput(
                attrs={"placeholder": "Enter a to-do item"}
            ),
        }
