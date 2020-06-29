from django.urls import path, include
from .views import create_customer, get_customer, all_customers


urlpatterns = [
	path('all', all_customers),
	path('register', create_customer),
	path('<int:id>',get_customer)
]
