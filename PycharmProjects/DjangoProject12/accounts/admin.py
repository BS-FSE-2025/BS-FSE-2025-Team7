from django.contrib import admin
from django.utils.html import format_html
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'description', 'display_photo', 'status', 'created_at')  # Added status and photo display
    search_fields = ('name', 'email', 'phone_number', 'description')
    list_filter = ('status', 'created_at')  # Filter by status and created date
    ordering = ('-created_at',)  # Order by latest created first

    # Allow inline editing of the status field
    list_editable = ('status',)

    # Customize how the photo field is displayed
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.photo.url)
        return "No Photo"
    display_photo.short_description = 'Photo'

    # Optional: Add custom admin actions for bulk updates
    actions = ['mark_as_in_progress', 'mark_as_done']

    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')  # Use lowercase status values
        self.message_user(request, "Selected reports marked as 'In Progress'.")

    def mark_as_done(self, request, queryset):
        queryset.update(status='done')  # Use lowercase status values
        self.message_user(request, "Selected reports marked as 'Done'.")

    mark_as_in_progress.short_description = "Mark selected reports as 'In Progress'"
    mark_as_done.short_description = "Mark selected reports as 'Done'"
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

from accounts.models import Login_1,Login_2,Register,Register2
from accounts.models import Login_3,Register,Register3

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

from django.contrib import admin
from .models import Register2, Login_2

class RegisterAdmin2(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Register2, RegisterAdmin2)
admin.site.register(Login_2)

admin.site.register(Register, RegisterAdmin)

admin.site.register(Register3, RegisterAdmin)
admin.site.register(Login_3)

admin.site.register(Login_1)
from django.contrib import admin

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'timestamp')  # הצגת שם המשתמש, תוכן ההודעה וזמן ההודעה
    search_fields = ('name', 'content')  # חיפוש לפי שם המשתמש ותוכן ההודעה
    list_filter = ('timestamp',)  # סינון לפי תאריך
    ordering = ('-timestamp',)  # מיון לפי זמן ההודעה (מהחדש לישן)

admin.site.register(Message, MessageAdmin)
