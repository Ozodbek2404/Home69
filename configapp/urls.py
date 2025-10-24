from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('order_details/', views.order_details, name='order_details'),

    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_order/', views.add_order, name='add_order'),
    path('add_order_detail/', views.add_order_detail, name='add_order_detail'),
]
