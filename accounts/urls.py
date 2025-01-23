from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),  # URL for registration page
    path('login/', views.login_, name='login'),  # URL for registration page

    path('login2/', views.login2, name='login2'),  # Updated to login2
    path('login3/', views.login3, name='login3'),  # Updated to login2

    path('register2/', views.register2, name='register2'),  # Updated to register2
    path('register3/', views.register3, name='register3'),  # Register page

]