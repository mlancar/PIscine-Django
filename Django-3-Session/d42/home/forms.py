from django.forms import ModelForm
from .models import Tip

class TipForm(ModelForm):
    class Meta:
        model = Tip
        fields = ['content']
