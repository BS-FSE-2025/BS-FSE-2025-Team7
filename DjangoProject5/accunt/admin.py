from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'created_at')  # Columns displayed in the list view
    list_filter = ('rating',)  # Add filtering by rating
    search_fields = ('comment',)  # Add search functionality for comments
    ordering = ('-created_at',)  # Order by creation date (newest first)

admin.site.register(Rating, RatingAdmin)
