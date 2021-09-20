from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['name', 'category', 'description']