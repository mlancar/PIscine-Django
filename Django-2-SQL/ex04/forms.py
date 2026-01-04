from django import forms

class MyForm(forms.Form):
    title = forms.ChoiceField(
        choices=[],
        widget=forms.Select(
            attrs={'class': 'form'}
        ),
        required=True,
    )
