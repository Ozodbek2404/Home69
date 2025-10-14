from django.shortcuts import render
from .models import *


def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    order = Order.objects.all()
    order_details = OrderDetail.objects.all()
    content = {
        "category": category,
        "product": product,
        "order": order,
        "order_detail": order_details
    }
    return render(request, 'index.html', content)


def category(request):
    category = Category.objects.all()
    content = {
        "category": category
    }
    return render(request, 'category.html', content)


def product(request):
    product = Product.objects.all()
    context = {
        "product": product
    }
    return render(request, 'product.html', context=context)


def order(request):
    order = Order.objects.all()
    content = {
        "order": order
    }
    return render(request, 'order.html', content)


def order_details(request):
    order_details = OrderDetail.objects.all()
    content = {
        "order_detail": order_details
    }
    return render(request, 'order_detail.html', content)
