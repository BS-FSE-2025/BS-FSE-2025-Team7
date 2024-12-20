from django.contrib import admin
from django.urls import path
from accounts import views  # חשוב: לייבא את views מתוך האפליקציה 'chat'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chat_view, name='chat'),  # דף הצ'אט הראשי
    path('send/', views.send_message, name='send_message'),  # שליחת הודעות
]
