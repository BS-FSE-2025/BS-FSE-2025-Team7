from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns
    path('', views.home, name='home'),
    path('report/', views.report_issue, name='report_issue'),
]

# Serve media files during development (if DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

