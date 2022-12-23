from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    product_img = models.ImageField(null = True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name