
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hadmin/', include('Hadmin.urls')),
    path('', include('Huser.urls')),
]
