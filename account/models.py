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
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Login_1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

from django.db import models
from django.contrib.auth.models import User

class Register2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ForeignKey to User
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Login_2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
