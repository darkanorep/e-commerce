from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product, Cart

def addtocart(response):
    if not response.user.is_authenticated:
        return redirect("/")

    if response.method != "POST":
        return redirect("/")

    product_id = int(response.POST.get("product_id"))

    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return JsonResponse({"status": "No such Product found"})

    quantity = int(response.POST.get("quantity"))
    size = response.POST.get("size")
    
    try:
        cart = Cart.objects.get(user=response.user, product_id=product_id, size=size)
        cart.quantity += quantity
        cart.save()

        return JsonResponse({"status": "Product Already in Cart"})

    except Cart.DoesNotExist:
        
        if quantity != 0:
            Cart.objects.create(user=response.user, product_id=product_id, quantity=quantity, size=size)
            return JsonResponse({"status": "Successfully Added"})

    return redirect("/")


def updatecart(response):
    if response.user.is_authenticated:
        if response.method != "POST":
            return JsonResponse({"status": "Invalid request method"})

        item_id = int(response.POST.get("item_id"))
        quantity = int(response.POST.get("quantity"))

        try:
            cart = Cart.objects.get(id=item_id)
        except Cart.DoesNotExist:
            return JsonResponse({"status": "No such Cart found"})

        cart.quantity += quantity
        cart.save()

        return JsonResponse({"status": "Successfully Added"})

    return redirect("/")

def removeitem(response, id):
    Cart.objects.filter(id=id).delete()

    return redirect("/cart")

