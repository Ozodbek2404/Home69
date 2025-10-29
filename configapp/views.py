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
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(
                category_name=form.cleaned_data['category_name'],
                description=form.cleaned_data['description'],
                picture=form.cleaned_data['picture']
            )
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'form.html', {'form': form, 'title': 'Kategoriya qo‘shish'})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            category_id = form.cleaned_data['category']
            category = get_object_or_404(Category, id=category_id)
            Product.objects.create(
                product_name=form.cleaned_data['product_name'],
                category=category,
                unit_price=form.cleaned_data['unit_price'],
                discontinued=form.cleaned_data['discontinued']
            )
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'form.html', {'form': form, 'title': 'Mahsulot qo‘shish'})


def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                customer_id=form.cleaned_data['customer_id'],
                order_date=form.cleaned_data['order_date'],
                required_date=form.cleaned_data['required_date'],
                shipped_date=form.cleaned_data['shipped_date']
            )
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'form.html', {'form': form, 'title': 'Buyurtma qo‘shish'})


def add_order_detail(request):
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data['order']
            product_id = form.cleaned_data['product']
            order = get_object_or_404(Order, id=order_id)
            product = get_object_or_404(Product, id=product_id)
            OrderDetail.objects.create(
                order=order,
                product=product,
                unit_price=form.cleaned_data['unit_price'],
                quantity=form.cleaned_data['quantity'],
                discount=form.cleaned_data['discount']
            )
            return redirect('index')
    else:
        form = OrderDetailForm()
    return render(request, 'form.html', {'form': form, 'title': 'Buyurtma tafsiloti qo‘shish'})
