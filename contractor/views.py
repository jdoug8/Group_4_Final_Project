from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Customer, Job, Bid
from .forms import CustomerForm, JobForm, BidForm

# Create your views here.

def home(request):
    return render(request, 'contractor/home.html', {})

def search(request):
    query = request.GET.get('q')
    customers = Customer.objects.filter(name__icontains=query)
    jobs = Job.objects.filter(customer_name__icontains=query)
    bids = Bid.objects.filter(customer__name__icontains=query)
    return render(request, 'contractor/search.html', {'customers': customers, 'bids': bids})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'contractor/customer_list.html', {'customers': customers})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_list', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'contractor/customer_edit.html', {'customer': customer})

def job_list(request):
    customer = Customer.objects.all()
    jobs = Job.objects.filter(customer=customer)
    return render(request, 'contractor/job_list.html', {'customer': customer, 'jobs': jobs})

def job_edit(request, pk):
    job = get_object_or_404(Bid, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('job_list', pk=job.pk)
    else:
        form = BidForm(instance=job)
    return render(request, 'contractor/job_edit.html', {'job': job})

def estimate_list(request):
    customer = Customer.objects.all()
    job = Job.objects.filter(customer=customer)
    estimates = Bid.objects.filter(job=job)
    return render(request, 'contractor/estimate_list.html', {'customer': customer, 'job': job, 'estimates': estimates})

def estimate_edit(request, pk):
    estimate = get_object_or_404(Bid, pk=pk)
    if request.method == "POST":
        form = BidForm(request.POST, instance=estimate)
        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.save()
            return redirect('estimate_list', pk=estimate.pk)
    else:
        form = BidForm(instance=estimate)
    return render(request, 'contractor/estimate_edit.html', {'estimate': estimate})