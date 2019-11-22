from django.db import models

# Create your models here.


class Product(models.Model):
    name= models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    brand = models.CharField(max_length=50, default="NA")
    pprice= models.IntegerField(default=0)
    price = models.IntegerField()


    def __str__(self):
        return self.name