from django import forms

from .models import Customer, Job, Bid

class CustomerForm(forms.ModelForm):

    class Meta:
        model= Customer
        fields = ('name','email', 'phone', 'address',)

class JobForm(forms.ModelForm):
    
    class Meta:
        model= Job
        fields = ('customer', 'description')
        
class BidForm(forms.ModelForm):
    
    class Meta:
        model = Bid
        fields = ('job','price')