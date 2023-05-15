from django.conf import settings
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    # Add any other relevant fields for customers
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name
    
class Job(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return str(self.customer)
    
class Bid(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.job)
