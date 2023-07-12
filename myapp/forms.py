from django import forms
from .models import Marca, Modelo, Cliente

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
