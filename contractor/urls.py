from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_bid, name='create_bid'),
    path('edit/<int:pk>/', views.edit_bid, name='edit_bid'),
    path('find/<int:pk>/', views.find_bid, name='find_bid'),
]
