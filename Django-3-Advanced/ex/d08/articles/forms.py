from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write Title...'
            }),
            'synopsis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write synopsis...',
                'rows': 5
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write article...',
                'rows': 5
            }),
        }