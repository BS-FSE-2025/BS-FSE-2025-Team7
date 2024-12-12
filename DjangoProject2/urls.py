# DjangoProject2/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    # Add your app-specific URLs here
    path('', include('account.urls')),  # Include account app URLs
]
