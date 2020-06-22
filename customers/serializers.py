from .models import customers
from rest_framework import serializers


class customersSerializer(serializers.ModelSerializer):
	class Meta:
		model = customers
		fields = ('id', 'issue_no', 'name', 'email', 'platform')