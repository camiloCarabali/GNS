from django.db import models


# Create your models here.

class Requests(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    method = models.CharField(max_length=100, null=False)
    consult = models.CharField(max_length=1000, null=False)
    dataReturn = models.CharField(max_length=10000, null=False)
