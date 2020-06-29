from django.urls import path, include
from .views import create_customer, get_customer, all_customers


urlpatterns = [
	path('allcustomers', all_customers),
	path('register', create_customer),
	path('customer/<int:id>',get_customer)
]
