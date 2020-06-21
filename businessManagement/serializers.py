from rest_framework import serializers

from .models import Receipts, Products


# class BusinessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Business
#         fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
