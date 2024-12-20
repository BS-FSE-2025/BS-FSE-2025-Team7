from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'timestamp')  # הצגת שם המשתמש, תוכן ההודעה וזמן ההודעה
    search_fields = ('name', 'content')  # חיפוש לפי שם המשתמש ותוכן ההודעה
    list_filter = ('timestamp',)  # סינון לפי תאריך
    ordering = ('-timestamp',)  # מיון לפי זמן ההודעה (מהחדש לישן)

admin.site.register(Message, MessageAdmin)
