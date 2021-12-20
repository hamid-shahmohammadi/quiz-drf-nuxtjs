from django.forms import ModelForm, PasswordInput
from .models import User
from django import forms

class UserForm(ModelForm):
    password = forms.CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = '__all__' 
        