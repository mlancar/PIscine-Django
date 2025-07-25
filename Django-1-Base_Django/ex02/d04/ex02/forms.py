from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label="Name", max_length=20)
    age = forms.IntegerField(label="Age", min_value=0)
    email = forms.EmailField(label="Email", required=False)