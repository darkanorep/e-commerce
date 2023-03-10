from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    stripe_id = models.CharField(max_length=250, null=True)
    product_img = models.ImageField(null = True, blank=True, upload_to='images/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.TextField(null = True, blank=True)
    quantity = models.IntegerField()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    review_img = models.ImageField(null = True, blank=True, upload_to='reviews/')

    def __str__(self):
        return self.comment