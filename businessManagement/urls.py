from django.urls import path

from .views import create_receipt, add_product_info_to_receipt

urlpatterns = [
    path('receipt/create',create_receipt),
    path('receipt/product',add_product_info_to_receipt)
]
