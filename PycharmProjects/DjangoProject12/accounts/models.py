from django.db import models

# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models

class Engineer(models.Model):
    name = models.CharField(max_length=100)
    # other fields related to the engineer

    def __str__(self):
        return self.name

class Report(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo = models.FileField(upload_to='uploads/', null=True, blank=True)  # Replace ImageField with FileField
    created_at = models.DateTimeField(auto_now_add=True)
    engineer = models.ForeignKey(Engineer, on_delete=models.SET_NULL, null=True, related_name="reports")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')  # Add this field


    def __str__(self):
        return f"Report by {self.name} at {self.created_at}"
from django.db import models
# adding changes :)
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)  # Allow null values
    email = models.EmailField()
    place=models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Login_1(models.Model):#citezen
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

from django.db import models
from django.contrib.auth.models import User

class Register2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    specialization  = models.CharField(max_length=15)
    work = models.CharField(max_length=15)
    email = models.EmailField()
    password1 = models.CharField(validators=[MinLengthValidator(8)], max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Login_2(models.Model):#engenner
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

from django.db import models

class Login_3(models.Model):#engenner
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
from django.db import models
from django.contrib.auth.models import User

class Register3(models.Model): #worker
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    work = models.CharField(max_length=15)
    email = models.EmailField()
    department=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    password1 = models.CharField(validators=[MinLengthValidator(8)], max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username
from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")  # שם משתמש
    content = models.TextField()  # תוכן ההודעה
    timestamp = models.DateTimeField(auto_now_add=True)  # זמן יצירת ההודעה

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"  # הצגה קצרה של ההודעה