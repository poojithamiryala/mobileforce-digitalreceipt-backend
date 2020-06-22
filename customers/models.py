from django.db import models


class customers(models.Model):
	issue_no = models.CharField(max_length = 10)
	name = models.CharField(max_length = 200)
	email = models.EmailField()
	platform = models.TextField(max_length = 50)
