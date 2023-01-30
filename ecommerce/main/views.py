from django.shortcuts import render, redirect

# Create your views here.
from django.conf import settings
from django.http.response import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import Product, Cart, Review
from .forms import AddProduct, clothesSize, menShoesSize, kidShoesSize, womenShoesSize


def index(response):
    if response.user.is_authenticated:
        cartNumber = Cart.objects.filter(user = response.user).count()
        return render(response, "main/index.html", {"cartNumber":cartNumber})

    return render(response, "main/index.html")

def products(response):
    p = Product.objects.all()
    if response.user.is_authenticated:
        cartNumber = Cart.objects.filter(user = response.user).count()
        return render(response, "main/products.html", {"p":p, "cartNumber":cartNumber})
    return render(response, "main/products.html", {"p":p})

def product(response, id):
    p = Product.objects.get(id=id)
    review = Review.objects.filter(product_id=id)
    
    men = menShoesSize()
    women = womenShoesSize()
    kid = kidShoesSize()
    clothes = clothesSize()

    if response.user.is_authenticated:
        cartNumber = Cart.objects.filter(user = response.user).count()
        return render(response, "main/product.html", {"p":p, "cartNumber":cartNumber, "review":review, "men":men, "women":women, "kid":kid, "clothes":clothes})
    
    return render(response, "main/product.html", {"p":p, "review":review})

def mycart(response):
    if response.user.is_authenticated:
        cart = Cart.objects.filter(user = response.user)
        cartNumber = Cart.objects.filter(user = response.user).count()

        return render(response, "main/cart.html", ({"cart": cart, "cartNumber":cartNumber}))

    return render(response, "main/cart.html")

def addproduct(response):
    if response.method == "POST":
        form = AddProduct(response.POST, response.FILES)

        if form.is_valid():
            n = form.cleaned_data["name"]
            g = form.cleaned_data["gender"]
            c = form.cleaned_data["category"]
            b = form.cleaned_data["brand"]
            d = form.cleaned_data["description"]
            pr = form.cleaned_data["price"]
            pic = form.cleaned_data["product_img"]

            p = Product(name = n, gender = g, category = c, brand = b, description = d, price = pr, product_img = pic)
            p.save()
            
        return HttpResponseRedirect("/products")
    
    else:
        form = AddProduct()

    return render(response, "main/addproduct.html", {"form":form})

def stripe_config(response):
    if response.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUB_KEY}
        return JsonResponse(stripe_config, safe=False)