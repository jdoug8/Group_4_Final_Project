from django.contrib import admin
from .models import Customer, Job, Bid

admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Bid)

# Register your models here.
