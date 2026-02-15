from django.forms import ModelForm
from .models import Tip
from django import forms


class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={
                'rows':4,
                'cols':40,
                'class': 'form-control',
                'placeholder': 'Write your Tip...'
                })
        }
    
    def clean_content(self):
        content = self.cleaned_data['content']
        return content.strip()
