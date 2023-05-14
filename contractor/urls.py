from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customer_list'),
    path('jobs/', views.job_list, name='job_list'),
    path('estimates/', views.estimate_list, name='estimate_list'),
    path('customers/edit/', views.customer_edit, name='customer_edit'),
    path('jobs/edit/', views.job_edit, name='job_edit'),
    path('estimate/edit/', views.estimate_edit, name='estimate_edit'),
]