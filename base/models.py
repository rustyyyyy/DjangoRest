from django.db import models
from datetime import date


class Brand(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class product(models.Model):
    brandname = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.IntegerField()
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name

