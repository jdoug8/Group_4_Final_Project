from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20,blank=True, null=True) 
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=20,blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

