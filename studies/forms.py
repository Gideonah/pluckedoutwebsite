from django import forms

class NameForm(forms.Form):
    symbol_key = forms.CharField(label='Search', max_length=100)