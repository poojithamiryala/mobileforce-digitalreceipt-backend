from django.core.validators import MinValueValidator
from django.db import models
import uuid

# Create your models here.
from userManagement.models import User


def add_one_to_receipt_number():
    """
    Returns the next default value for the `ones` field, starts with
    1
    """
    largest = Receipts.objects.all().order_by('receipt_number').last().receipt_number
    if not largest:
        return 1
    return largest + 1


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=False)
    email_address = models.CharField(unique=True, max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Receipts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    receipt_number = models.IntegerField(default=add_one_to_receipt_number)  # need to customize this
    description = models.CharField(max_length=1000, unique=False)
    amount = models.FloatField()
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    receipt = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
