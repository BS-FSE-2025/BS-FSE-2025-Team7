# DjangoProject2/urls.py
from django.contrib import admin
from django.urls import path, include
from account import views  # Correct the import statement

urlpatterns = [
    path('register/', views.register, name='register'),  # URL for registration page
    path('', views.home, name='home'),  # URL for registration page
    path('login/', views.login_, name='login'),  # URL for registration page

    path('login2/', views.login2, name='login2'),  # Updated to login2
    path('register2/', views.register2, name='register2'),  # Updated to register2

]
