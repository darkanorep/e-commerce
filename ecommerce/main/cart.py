from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product, Cart

def addtocart(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            product_id = int(response.POST.get("product_id"))
            product_check = Product.objects.get(id=product_id)
            quantity = int(response.POST.get("quantity"))
            size = response.POST.get("size")

            if (product_check):
                if (Cart.objects.filter(user=response.user.id, size=size)):
                        
                    cart = Cart.objects.get(user = response.user, product_id=product_id, size=size)
                    cart.quantity += quantity
                    print(size)
                    cart.save()

                    return JsonResponse({"status": "Product Already in Cart"})
                else:

                    if quantity != 0 :
                        Cart.objects.create(user = response.user, product_id=product_id, quantity=quantity, size=size)
                
                    return JsonResponse({"status":" Successfully Added"})
            else:
                return JsonResponse({"status":" No such Product found"})
            
        return redirect("/")
    
    return redirect("/")

def updatecart(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            item_id = int(response.POST.get("item_id"))
            quantity = int(response.POST.get("quantity"))

            cart = Cart.objects.get(id = item_id)

            cart.quantity += quantity
            cart.save()
                
            return JsonResponse({"status": "Product Already in Cart"})
        
        return JsonResponse({"status":" Successfully Added"})

    return redirect("/")

def removeitem(response, id):
    Cart.objects.filter(id=id).delete()

    return redirect("/cart")

