from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('category/', category),
    path('product/', product),
    path('order/', order),
    path('order_detail/', order_details)
]