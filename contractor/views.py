from django.shortcuts import redirect, render
from .models import Customer, Job, Bid

# Create your views here.

def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('q')
    customers = Customer.objects.filter(name__icontains=query)
    bids = Bid.objects.filter(customer__name__icontains=query)
    return render(request, 'search.html', {'customers': customers, 'bids': bids})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def job_list(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    jobs = Job.objects.filter(customer=customer)
    return render(request, 'job_list.html', {'customer': customer, 'jobs': jobs})

def create_estimate(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        price = request.POST.get('price')
        bid = Bid.objects.create(job=job, price=price)
        return redirect('job_list', customer_id=job.customer.id)
    return render(request, 'create_estimate.html', {'job': job})