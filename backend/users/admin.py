from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.hashers import make_password
from .form import UserForm

class changePass(admin.ModelAdmin):
    form=UserForm
    
    def save_model(self, request, obj, form, change):
        obj.password =  make_password(obj.password)
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(User,changePass)