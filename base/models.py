from django.db import models
import datetime
# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    brandname = models.CharField(max_length=250)
    
    def __str__(self):
        return self.brandname
