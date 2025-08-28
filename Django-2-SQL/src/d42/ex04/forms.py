from django import forms

class MyForm(forms.Form):
    title = forms.SelectMultiple()
