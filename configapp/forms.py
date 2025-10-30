from django import forms
from .models import Category, Product, Order, OrderDetail
from datetime import date
import re


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_category_name(self):
        name = self.cleaned_data.get('category_name')
        if not name[0].isupper():
            raise forms.ValidationError("Birinchi harf katta bo‘lishi kerak.")
        if any(ch.isdigit() for ch in name):
            raise forms.ValidationError("Kategoriya nomida raqam bo‘lmasin.")
        return name


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        name = self.cleaned_data.get('product_name')
        if re.search(r'[^A-Za-z\s]', name):
            raise forms.ValidationError("Mahsulot nomida raqam yoki tinish belgisi bo‘lmasin.")
        return name

    def clean_unit_price(self):
        price = self.cleaned_data.get('unit_price')
        if price < 1 or price > 10:
            raise forms.ValidationError("Narx 1$ dan baland, 10$ dan past bo‘lishi kerak.")
        return price


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def clean_order_date(self):
        order_date = self.cleaned_data.get('order_date')
        if order_date < date(2025, 1, 1):
            raise forms.ValidationError("Buyurtma sanasi 2025-01-01 dan katta bo‘lishi kerak.")
        return order_date


class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'




