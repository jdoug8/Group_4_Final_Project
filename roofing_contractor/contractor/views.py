# views.py in the contractor app
from django.shortcuts import render
from .models import Customer, Bid

def home(request):
    return render(request, 'contractor/home.html')

def search(request):
    query = request.GET.get('q')
    customers = Customer.objects.filter(name__icontains=query)
    bids = Bid.objects.filter(customer__name__icontains=query)
    return render(request, 'contractor/search.html', {'customers': customers, 'bids': bids})

def create(request):
    if request.method == 'POST':
        # Save the customer and bid data
        return redirect('home')
    return render(request, 'contractor/create.html')

def edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        # Update the customer and bid data
        return redirect('home')
    return render(request, 'contractor/edit.html', {'customer': customer})

def find(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    bids = Bid.objects.filter(customer=customer)
    return render(request, 'contractor/find.html', {'customer': customer, 'bids': bids})
