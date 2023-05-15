from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:id>/', views.customer_detail, name='customer_detail'),
    path('customers/new/', views.customer_new, name='customer_new'),
    path('customers/<int:id>/edit/', views.customer_edit, name='customer_edit'),
    
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:id>/', views.job_detail, name='job_detail'),
    path('jobs/new/', views.job_new, name='job_new'),
    path('jobs/<int:id>/edit/', views.job_edit, name='job_edit'),
    
    path('estimates/', views.estimate_list, name='estimate_list'),
    path('estimates/<int:id>/', views.estimate_detail, name='estimate_detail'),
    path('estimates/new/', views.estimate_new, name='estimate_new'),
    path('estimates/<int:id>/edit/', views.estimate_edit, name='estimate_edit'),
]