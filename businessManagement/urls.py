from django.urls import path
from .views import create_business, get_business
from .views import create_receipt, add_product_info_to_receipt, get_all_receipt, get_all_draft_receipt

urlpatterns = [
    path('receipt/create',create_receipt),
    path('receipt/product',add_product_info_to_receipt),
    path('receipt/issued',get_all_receipt),
    path('receipt/draft',get_all_draft_receipt),
    path('info/create', create_business),
    path('info/all', get_business)

]
