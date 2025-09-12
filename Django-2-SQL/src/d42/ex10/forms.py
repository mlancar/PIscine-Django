from django import forms

class MyForm(forms.Form):
    min_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="minimum date of release"
    )
    max_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="maximum date of release"
    )

    diameter = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number'}),
        label="PLanet diameter",
        min_value=0
    )

