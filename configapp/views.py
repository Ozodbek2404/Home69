from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    context = {
        "category": Category.objects.all(),
        "product": Product.objects.all(),
        "order": Order.objects.all(),
        "order_detail": OrderDetail.objects.all()
    }
    return render(request, 'index.html', context)


def category(request):
    return render(request, 'category.html', {"category": Category.objects.all()})


def product(request):
    return render(request, 'product.html', {"product": Product.objects.all()})


def order(request):
    return render(request, 'order.html', {"order": Order.objects.all()})


def order_details(request):
    return render(request, 'order_detail.html', {"order_detail": OrderDetail.objects.all()})


def add_category(request):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('category')
    return render(request, 'form.html', {'form': form, 'title': 'Kategoriya qo‘shish'})


def add_product(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product')
    return render(request, 'form.html', {'form': form, 'title': 'Mahsulot qo‘shish'})


def add_order(request):
    form = OrderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('order')
    return render(request, 'form.html', {'form': form, 'title': 'Buyurtma qo‘shish'})


def add_order_detail(request):
    form = OrderDetailForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('order_details')
    return render(request, 'form.html', {'form': form, 'title': 'Buyurtma tafsiloti qo‘shish'})
