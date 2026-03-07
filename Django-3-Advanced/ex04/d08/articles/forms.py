from django import forms
from articles.models import Article
from django.utils.translation import gettext_lazy as _

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']
        labels = {
            'title': _('Title'),
            'synopsis': _('Synopsis'),
            'content': _('Content'),
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _("Write Title...")
            }),
            'synopsis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _("Write synopsis..."),
                'rows': 5
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _("Write content..."),
                'rows': 5
            }),
        }