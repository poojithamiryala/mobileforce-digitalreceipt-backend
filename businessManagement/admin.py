from django.contrib import admin

# Register your models here.
from .models import Receipts,Products

admin.site.register(Receipts)
admin.site.register(Products)