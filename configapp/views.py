from django.shortcuts import render, redirect, get_object_or_404
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


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('index')


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('index')


def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('index')


def delete_order_detail(request, id):
    detail = get_object_or_404(OrderDetail, id=id)
    detail.delete()
    return redirect('index')
