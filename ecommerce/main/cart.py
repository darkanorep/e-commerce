from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product, Cart



def addtocart(response):
    if response.method == "POST":
        product_id = int(response.POST.get("product_id"))
        product_check = Product.objects.get(id=product_id)

        if (product_check):
            if (Cart.objects.filter(user=response.user.id, product_id=product_id)):
                
                return JsonResponse({"status": "Product Already in Cart"})
            else:
                quantity = int(response.POST.get("quantity"))

                Cart.objects.create(user = response.user, product_id=product_id, quantity=quantity)
                return JsonResponse({"status":" Successfully Added"})
        else:
            return JsonResponse({"status":" No such Product found"})
    
    return redirect("/")