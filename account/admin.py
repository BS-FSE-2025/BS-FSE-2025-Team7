from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

from account.models import Login_1,Login_2,Register,Register2

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

from django.contrib import admin
from .models import Register2, Login_2

class RegisterAdmin2(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(Register2, RegisterAdmin2)
admin.site.register(Login_2)

admin.site.register(Register, RegisterAdmin)


admin.site.register(Login_1)
