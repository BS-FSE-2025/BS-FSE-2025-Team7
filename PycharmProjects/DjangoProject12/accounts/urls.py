from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns
    path('', views.home, name='home'),
    path('report/', views.report_issue, name='report_issue'),
    path('register/', views.register, name='register'),  # URL for registration page
    path('login/', views.login_, name='login'),  # URL for registration page
    path('map/', views.reports_map, name='reports_map'),  # Add the map view
    path('delete_report/<int:report_id>/', views.delete_report, name='delete_report'),

    path('login2/', views.login2, name='login2'),  # Updated to login2
    path('login3/', views.login3, name='login3'),  # Updated to login2

    path('register2/', views.register2, name='register2'),  # Updated to register2
    path('register3/', views.register3, name='register3'),  # Register page
    path('setezin_map/', views.setezin_map, name='setezin_map'),
    path('chat/', views.chat_view, name='chat'),  # דף הצ'אט הראשי
    path('send/', views.send_message, name='send_message'),
    path('update_status/<int:report_id>/', views.update_status, name='update_status'),

]

# Serve media files during development (if DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
