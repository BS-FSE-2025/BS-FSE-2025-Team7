from django.urls import path
from django.shortcuts import redirect
from accunt import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lambda request: redirect('rate/')),  # Redirect root URL to rate/
    path('rate/', views.rate_complaint, name='rate_complaint'),
    path('success/', views.success_page, name='success'),
]
