from django.shortcuts import render
from .models import Product

def add_variable_to_context(response):
    categories = Product.objects.values('category').distinct()
    return ({'categories': categories})