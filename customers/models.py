from django.db import models


class customers(models.Model):
    issue_no = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    platform = models.TextField(max_length=50)


class CustomerDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    platform = models.CharField(max_length=50, null=True)
    phoneNumber = models.CharField(max_length=50, null=False)
    user = models.CharField(max_length=200, null=False)
