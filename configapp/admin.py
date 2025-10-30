from django.contrib import admin
from .models import *

# admin.site.register([Category, Product, Order, OrderDetail])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description', 'picture')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'unit_price', 'discontinued')


@admin.register(Order)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'order_date', 'required_date', 'shipped_date')


@admin.register(OrderDetail)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'unit_price', 'quantity', 'discount')

