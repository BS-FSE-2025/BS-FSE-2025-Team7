from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo = models.FileField(upload_to='uploads/', null=True, blank=True)  # Replace ImageField with FileField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.name} at {self.created_at}"
