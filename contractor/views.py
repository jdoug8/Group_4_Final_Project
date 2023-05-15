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
    return render(request, 'contractor/search.html', {'customers': customers, 'jobs': jobs, 'bids': bids})

def customer_list(request):
    customers = Customer.objects.order_by('name')
    return render(request, 'contractor/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'contractor/customer_detail.html', {'customer': customer})

def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_list', id=customer.id)
    else:
        form = CustomerForm()
    return render(request, 'contractor/customer_edit.html', {'form': form})

def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.name = request.user
            customer.save()
            return redirect('customer_list', id=customer.id)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'contractor/customer_edit.html', {'customer': customer})

def job_list(request):
    jobs = Job.objects.order_by('customer')
    return render(request, 'contractor/job_list.html', {'jobs': jobs})

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'contractor/job_detail.html', {'job': job})

def job_new(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('job_list', id=job.id)
    else:
        form = CustomerForm()
    return render(request, 'contractor/job_edit.html', {'form': form})

def job_edit(request, id):
    job = get_object_or_404(Bid, id=id)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('job_list', id=job.id)
    else:
        form = BidForm(instance=job)
    return render(request, 'contractor/job_edit.html', {'job': job})

def estimate_list(request):
    estimates = Bid.objects.order_by('job')
    return render(request, 'contractor/estimate_list.html', {'estimates': estimates})

def estimate_detail(request, id):
    estimate = get_object_or_404(Bid, id=id)
    return render(request, 'contractor/estimate_detail.html', {'estimate': estimate})

def estimate_new(request):
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.save()
            return redirect('estimate_list', id=estimate.id)
    else:
        form = BidForm()
    return render(request, 'contractor/estimate_edit.html', {'form': form})

def estimate_edit(request, id):
    estimate = get_object_or_404(Bid, id=id)
    if request.method == "POST":
        form = BidForm(request.POST, instance=estimate)
        if form.is_valid():
            estimate = form.save(commit=False)
            estimate.save()
            return redirect('estimate_list', id=estimate.id)
    else:
        form = BidForm(instance=estimate)
    return render(request, 'contractor/estimate_edit.html', {'estimate': estimate})