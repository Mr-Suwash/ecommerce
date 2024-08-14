from django.db import models

# Create your models here.

class product(models.Model):
    Name = models.CharField((""), max_length=50)
    Price = models.FloatField((""))
    Discount = models.FloatField((""))
    Description = models.TextField((""))
    Image =models.CharField((""), max_length=500)
    Category = models.CharField((""), max_length=50)