from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


# middleware -to verify token present in headers and pass user in request object
# create/update bussiness ,receipt details
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Receipts
from .serializers import ReceiptSerializer, ProductSerializer


def add_one_to_receipt_number(user):
    """
    Returns the next default value for the `ones` field, starts with
    1
    """
    largest = Receipts.objects.filter(user=user).order_by('receipt_number').last()
    if not largest:
        return 1
    return largest.receipt_number + 1


@api_view(['POST'])
def create_receipt(request):
    if request.method == 'POST':
        print(request.user_id)
        data = {
            'user': request.user_id,
            'receipt_number':add_one_to_receipt_number(request.user_id)
        }
        print(data)
        serializer = ReceiptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_product_info_to_receipt(request):
    # send the receipt id
    if request.method == 'POST':
        # user
        data = {
            'receipt': request.data['receiptId'],
            'name': request.data['name'],
            'quantity': request.data['quantity'],
            'amount': request.data['amount']
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
