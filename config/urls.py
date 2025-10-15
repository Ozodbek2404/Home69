from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('configapp.urls')),
    path('category/', include('configapp.urls')),
    path('product/', include('configapp.urls')),
    path('order/', include('configapp.urls')),
    path('order_detail/', include('configapp.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
