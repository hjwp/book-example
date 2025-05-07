from django import forms


class ItemForm(forms.Form):
    item_text = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Enter a to-do item",
                "class": "form-control form-control-lg",
            }
        ),
    )
