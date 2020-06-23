from .models import customers, CustomerDetails
from rest_framework import serializers


class customersSerializer(serializers.ModelSerializer):
    class Meta:
        model = customers
        fields = ('id', 'issue_no', 'name', 'email', 'platform')


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'
