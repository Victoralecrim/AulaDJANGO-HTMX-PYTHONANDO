# forms.py

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Relaciona o formulário com o modelo Product
        fields = ['name', 'price']  # Campos do formulário
