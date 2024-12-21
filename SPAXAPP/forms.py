# forms.py
from django import forms # type: ignore
from .models import Product, Store

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'inventory_count', 'serial_no', 'expiry_date']

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'location', 'contact_info', 'products', 'sensors', 'latitude', 'longitude']
        widgets = {
            'products': forms.CheckboxSelectMultiple,
        }
