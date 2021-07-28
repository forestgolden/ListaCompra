from django.forms import ModelForm
from .models import ModelTipoItem

class TipoItemForm(ModelForm):
    class Meta:
        model = ModelTipoItem
        fields = ['tipo_nome']
