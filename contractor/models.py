from django.conf import settings
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    # Add any other relevant fields for customers
    
class Bid(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    estimate = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # Add any other relevant fields for bids

