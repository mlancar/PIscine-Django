from django import forms

class MyForm(forms.Form):
    title = forms.ChoiceField(
        choices=[],
        widget=forms.Select(
            attrs={'class': 'form'}
        ),
        required=True,
        
    )
    text = forms.CharField(
        max_length=100,
        label= "Opening Crawl",
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 40,
            'placeholder': 'Write something...'
        })
    )
