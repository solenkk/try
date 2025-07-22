from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home),                 # Homepage (empty path)
    path('customer/', views.customer),     # Customer page
    path('product/', views.product),       # Product page
]