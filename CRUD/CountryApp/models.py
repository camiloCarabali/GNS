from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    population = models.IntegerField()

    class Meta:
        db_table = 'country'
