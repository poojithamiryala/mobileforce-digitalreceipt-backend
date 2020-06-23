from django.core.validators import MinValueValidator
from django.db import models
import uuid

# Create your models here.
from userManagement.models import User


class Receipts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receipt_number = models.IntegerField()  # need to customize this
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    receipt = models.ForeignKey(Receipts, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=100)
    quantity = models.PositiveIntegerField(null=True, validators=[MinValueValidator(1)])
    amount = models.FloatField(null=True, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    message = models.CharField(null=True, max_length=100)
    date_to_deliver = models.DateField(null=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)