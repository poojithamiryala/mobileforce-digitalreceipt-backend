import json
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from .models import customers
from .serializers import customersSerializer


class indexViewSet(viewsets.ModelViewSet):
	queryset = customers.objects.all().order_by('name')
	serializer_class = customersSerializer

def single(request, id):
	customer = customers.objects.get(id = id)
	return JsonResponse(customer, safe = False)
		

