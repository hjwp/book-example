from django import forms

from lists.models import Item


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ("text",)

    # item_text = forms.CharField(
    #     widget=forms.widgets.TextInput(
    #         attrs={
    #             "placeholder": "Enter a to-do item",
    #             "class": "form-control form-control-lg",
    #         }
    #     ),
    # )
