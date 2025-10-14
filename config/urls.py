
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('configapp.urls')),
    path('category/', include('configapp.urls')),
    path('product/', include('configapp.urls')),
    path('order/', include('configapp.urls')),
    path('order_detail/', include('configapp.urls'))
]
