from django import forms

from .models import Customer, Job, Bid

class CustomerForm(forms.ModelForm):

    class Meta:
        model_1 = Customer
        fields = ('name', 'text',)

class JobForm(forms.ModelForm):
    
    class Meta:
        model_2 = Job
        fields = ('name', 'text')
        
class BidForm(forms.ModelForm):
    
    class Meta:
        model_3 = Bid
        fields = ('name','text')