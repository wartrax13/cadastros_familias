from django import forms
from .models import Familias


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Familias
        fields = '__all__'
