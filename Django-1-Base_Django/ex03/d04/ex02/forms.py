from django import forms

class MyForm(forms.Form):
    login = forms.CharField(label="Login", max_length=20)
    # note = forms.IntegerField(label="Note", min_value=0)
    commentaire = forms.CharField(
        label="Commentaire",
        # required=False,
        max_length=250,
        widget=forms.Textarea(attrs={
            'rows': 4,        
            'cols': 40,
            'placeholder': 'Écrivez votre commentaire ici...'
        })
    )