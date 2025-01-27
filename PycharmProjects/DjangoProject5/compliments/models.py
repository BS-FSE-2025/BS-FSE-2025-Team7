from django.db import models

class Compliment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # longitude

    def __str__(self):
        return f"Compliment by {self.name}"
