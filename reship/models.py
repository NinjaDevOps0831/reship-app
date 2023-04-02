from django.db import models
from django.contrib.auth.models import User

# Create your models here.

## User Additional Information
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    email = models.EmailField(max_length = 200, unique = True)
    phone = models.CharField(max_length = 20, null = True)
    country = models.CharField(max_length = 2)

    indexes = [
        models.Index(fields = ['email'])
    ]

## Contact Messages
class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 20, null = True)
    messages = models.JSONField()