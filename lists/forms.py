from django import forms

class ItemForm(forms.Form):
    item_text = forms.CharField()
