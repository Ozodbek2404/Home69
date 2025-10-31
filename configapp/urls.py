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

    path('delete/category/<int:id>/', views.delete_category, name='delete_category'),
    path('delete/product/<int:id>/', views.delete_product, name='delete_product'),
    path('delete/order/<int:id>/', views.delete_order, name='delete_order'),
    path('delete/detail/<int:id>/', views.delete_order_detail, name='delete_order_detail'),

    path('update_category/<int:id>/', views.update_category, name='update_category'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('update_order/<int:id>/', views.update_order, name='update_order'),
    path('update_order_detail/<int:id>/', views.update_order_detail, name='update_order_detail'),
]
