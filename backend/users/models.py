from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_length(value):
    
    if len(value) < 6:
        raise ValidationError(
            _('password is less than 6'),
            params={'value': value},
        )


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255,validators=[validate_length])
    username = None

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['password']
