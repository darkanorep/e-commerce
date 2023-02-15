from django.shortcuts import render
from .models import Product

def add_variable_to_context(response):
    catalog = Product.objects.values('gender').distinct()
    return ({'catalog': catalog})