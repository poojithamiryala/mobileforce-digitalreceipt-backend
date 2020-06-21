from django.db import models

# Create your models here.


from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=False)
    email_address = models.CharField(unique=True, max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
