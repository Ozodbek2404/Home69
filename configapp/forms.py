# from django import forms
# from .models import Category, Product, Order, OrderDetail
# from datetime import date
# import re
#
#
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = '__all__'
#
#     def clean_category_name(self):
#         name = self.cleaned_data.get('category_name')
#         if not name[0].isupper():
#             raise forms.ValidationError("Birinchi harf katta bo‘lishi kerak.")
#         if any(ch.isdigit() for ch in name):
#             raise forms.ValidationError("Kategoriya nomida raqam bo‘lmasin.")
#         return name
#
#
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def clean_product_name(self):
#         name = self.cleaned_data.get('product_name')
#         if re.search(r'[^A-Za-z\s]', name):
#             raise forms.ValidationError("Mahsulot nomida raqam yoki tinish belgisi bo‘lmasin.")
#         return name
#
#     def clean_unit_price(self):
#         price = self.cleaned_data.get('unit_price')
#         if price < 1 or price > 10:
#             raise forms.ValidationError("Narx 1$ dan baland, 10$ dan past bo‘lishi kerak.")
#         return price
#
#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#
#     def clean_order_date(self):
#         order_date = self.cleaned_data.get('order_date')
#         if order_date < date(2025, 1, 1):
#             raise forms.ValidationError("Buyurtma sanasi 2025-01-01 dan katta bo‘lishi kerak.")
#         return order_date
#
#
# class OrderDetailForm(forms.ModelForm):
#     class Meta:
#         model = OrderDetail
#         fields = '__all__'








from django import forms
from datetime import date
import re


class CategoryForm(forms.Form):
    category_name = forms.CharField(label="Kategoriya nomi", max_length=100)
    description = forms.CharField(
        label="Tavsif", widget=forms.Textarea(attrs={"rows": 3}), required=False
    )
    picture = forms.ImageField(required=False)

    def clean_category_name(self):
        name = self.cleaned_data.get('category_name')
        if not name[0].isupper():
            raise forms.ValidationError("Birinchi harf katta bo‘lishi kerak.")
        if any(ch.isdigit() for ch in name):
            raise forms.ValidationError("Kategoriya nomida raqam bo‘lmasin.")
        return name


class ProductForm(forms.Form):
    product_name = forms.CharField(label="Mahsulot nomi", max_length=100)
    category = forms.IntegerField(label="Kategoriya ID raqami")
    unit_price = forms.DecimalField(label="Narx ($)", max_digits=10, decimal_places=2)
    discontinued = forms.BooleanField(label="Faol emas", required=False)

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


class OrderForm(forms.Form):
    customer_id = forms.CharField(label="Mijoz ID", max_length=50)
    order_date = forms.DateField(label="Buyurtma sanasi", widget=forms.DateInput(attrs={"type": "date"}))
    required_date = forms.DateField(label="Talab qilingan sana", widget=forms.DateInput(attrs={"type": "date"}))
    shipped_date = forms.DateField(label="Yuborilgan sana", widget=forms.DateInput(attrs={"type": "date"}), required=False)

    def clean_order_date(self):
        order_date = self.cleaned_data.get('order_date')
        if order_date < date(2025, 1, 1):
            raise forms.ValidationError("Buyurtma sanasi 2025-01-01 dan katta bo‘lishi kerak.")
        return order_date


class OrderDetailForm(forms.Form):
    order = forms.IntegerField(label="Buyurtma ID")
    product = forms.IntegerField(label="Mahsulot ID")
    unit_price = forms.DecimalField(label="Narx ($)", max_digits=10, decimal_places=2)
    quantity = forms.IntegerField(label="Soni")
    discount = forms.DecimalField(label="Chegirma (%)", max_digits=4, decimal_places=2, required=False)
