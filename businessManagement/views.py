from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# middleware -to verify token present in headers and pass user in request object
# create/update bussiness ,receipt details
from rest_framework import status
from rest_framework.decorators import api_view
from customers.models import CustomerDetails
from customers.serializers import CustomersSerializer
from userManagement.models import User
from userManagement.serializers import UserSerializer
from .models import Receipts, Products
from .serializers import ReceiptSerializer, ProductSerializer


def add_one_to_receipt_number(user):
    """
    Returns the next default value for the `ones` field, starts with
    1
    """
    largest = (
        Receipts.objects.filter(user=user, receipt_number__startswith="R-")
        .order_by("receipt_number")
        .last()
    )
    if not largest:
        return 1
    return "R-" + largest.receipt_number + 1


@api_view(["POST"])
def create_receipt(request):
    if request.method == "POST":
        if "customerId" not in request.data:
            return JsonResponse(
                {"error": "Enter customerId"}, status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            "user": request.user_id,
            "customer": request.data["customerId"],
            "receipt_number": 1,
        }
        serializer = ReceiptSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def add_product_info_to_receipt(request):
    # send the receipt id
    if request.method == "POST":
        if "receiptId" not in request.data:
            return JsonResponse(
                {"error": "Enter receiptId"}, status=status.HTTP_400_BAD_REQUEST
            )
        if "name" not in request.data:
            return JsonResponse(
                {"error": "Enter product name"}, status=status.HTTP_400_BAD_REQUEST
            )
        if "quantity" not in request.data:
            return JsonResponse(
                {"error": "Enter quantity"}, status=status.HTTP_400_BAD_REQUEST
            )
        if "unit_price" not in request.data:
            return JsonResponse(
                {"error": "Enter unit_price"}, status=status.HTTP_400_BAD_REQUEST
            )
        # user
        data = {
            "receipt": request.data["receiptId"],
            "name": request.data["name"],
            "quantity": request.data["quantity"],
            "unit_price": request.data["unit_price"],
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_receipt(request):
    # send the receipt id
    if request.method == "GET":
        try:
            recipt = Receipts.objects.filter(user=request.user_id, issued=True)
            if recipt:
                user = User.objects.get(id=request.user_id)
                userData = UserSerializer(user, many=False).data
                receipts = ReceiptSerializer(recipt, many=True).data
                for data in receipts:
                    data["user"] = {
                        "id": userData["id"],
                        "name": userData["name"],
                        "email_address": userData["email_address"],
                    }
                    products = Products.objects.filter(receipt=data["id"])
                    products_data = ProductSerializer(products, many=True).data
                    data["products"] = products_data
                    print(data["products"])
                    customer = CustomerDetails.objects.get(pk=data["customer"])
                    data["customer"] = CustomersSerializer(customer, many=False).data
                    data["total"] = sum(
                        c["unit_price"] * c["quantity"] for c in data["products"]
                    )
                return JsonResponse(
                    {"message": "Retreived all receipts", "data": receipts},
                    status=status.HTTP_200_OK,
                )
            else:
                return JsonResponse(
                    {"message": "There are no receipts created"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as error:
            return JsonResponse({"message": error}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_draft_receipt(request):
    # send the receipt id
    if request.method == "GET":
        try:
            draftReceipt = Receipts.objects.filter(user=request.user_id, issued=False)
            if draftReceipt:
                user = User.objects.get(id=request.user_id)
                userData = UserSerializer(user, many=False).data
                draftReceipts = ReceiptSerializer(draftReceipt, many=True).data
                for data in draftReceipts:
                    data["user"] = {
                        "id": userData["id"],
                        "name": userData["name"],
                        "email_address": userData["email_address"],
                    }
                    products = Products.objects.filter(receipt=data["id"])
                    products_data = ProductSerializer(products, many=True).data
                    data["products"] = products_data
                    print(data["products"])
                    customer = CustomerDetails.objects.get(pk=data["customer"])
                    data["customer"] = CustomersSerializer(customer, many=False).data
                    data["total"] = sum(
                        c["unit_price"] * c["quantity"] for c in data["products"]
                    )
                return JsonResponse(
                    {
                        "message": "Retreived all drafted receipts",
                        "data": draftReceipts,
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return JsonResponse(
                    {"message": "There are no draft receipts created"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as error:
            return JsonResponse({"message": error}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def customize_receipt(request):
    if request.method == "POST":
        try:
            if "customerId" not in request.data:
                return JsonResponse(
                    {"error": "Enter customerId"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "signature" not in request.data:
                return JsonResponse(
                    {"error": "Upload Signature"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "customerName" not in request.data:
                return JsonResponse(
                    {"error": "Enter Customer name"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "email" not in request.data:
                return JsonResponse(
                    {"error": "Enter email Address"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "address" not in request.data:
                return JsonResponse(
                    {"error": "Enter address"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "phoneNumber" not in request.data:
                return JsonResponse(
                    {"error": "Phone Number"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "unit_price" not in request.data:
                return JsonResponse(
                    {"error": "Enter unit_price"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "receiptId" not in request.data:
                return JsonResponse(
                    {"error": "Enter receiptId"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "productName" not in request.data:
                return JsonResponse(
                    {"error": "Enter product name"}, status=status.HTTP_400_BAD_REQUEST
                )
            if "quantity" not in request.data:
                return JsonResponse(
                    {"error": "Enter quantity"}, status=status.HTTP_400_BAD_REQUEST
                )

            errorsDict = {}
            data = {}

            receiptData = {
                "user": request.user_id,
                "customer": request.data["customerId"],
                "signature": request.data["signature"],
                "font": request.data.get("font"),
                "color": request.data.get("color"),
                "paid_stamp": request.data.get("paidStamp"),
            }

            receiptSerializer = ReceiptSerializer(data=receiptData)

            customerData = {
                "name": request.data["customerName"],
                "email": request.data["email"],
                "phoneNumber": request.data["phoneNumber"],
                "address": request.data["address"],
                "user": request.user_id,
                "saved": True if request.data.get("saved") else False,
            }

            customerSerializer = CustomersSerializer(data=customerData)

            productData = {
                "receipt": request.data["receiptId"],
                "name": request.data["productName"],
                "quantity": request.data["quantity"],
                "part_payment": request.data.get("part_payment", 0),
                "unit_price": request.data["unit_price"],
            }

            productSerializer = ProductSerializer(data=productData)

            is_receipt_valid = receiptSerializer.is_valid()
            is_product_valid = productSerializer.is_valid()
            is_customer_valid = customerSerializer.is_valid()

            if is_receipt_valid and is_product_valid and is_customer_valid:
                receiptSerializer.save()
                productSerializer.save()
                customerSerializer.save()
                data["receipt"] = receiptSerializer.data
                data["product"] = productSerializer.data
                data["customer"] = customerSerializer.data

                return JsonResponse(data, status=status.HTTP_200_OK)

            else:
                errorsDict = {}

                errorsDict.update(receiptSerializer.errors)
                errorsDict.update(productSerializer.errors)
                errorsDict.update(customerSerializer.errors)

                return JsonResponse(errorsDict, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
