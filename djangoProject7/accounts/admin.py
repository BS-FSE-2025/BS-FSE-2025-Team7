from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('name', 'email', 'phone_number', 'created_at', 'latitude', 'longitude')

    # Fields to search by in the list view
    search_fields = ('name', 'email', 'phone_number')

    # Exclude created_at from the admin form (since it should not be editable)
    exclude = ('created_at',)

    # Make 'created_at' read-only in the admin form
    readonly_fields = ('created_at',)

    # Optional: customize the layout in the admin form using fieldsets
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number', 'description', 'latitude', 'longitude', 'photo')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # Makes the created_at field collapsible, but it will be read-only
        }),
    )


# Register the Report model with the customized ReportAdmin
admin.site.register(Report, ReportAdmin)
