from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .forms import AddProduct

def index(response):
    return render(response, "main/index.html")

def products(response):
    p = Product.objects.all()
    return render(response, "main/products.html", {"p":p})

def product(response, id):
    p = Product.objects.get(id=id)
    return render(response, "main/product.html", {"p":p})

def addproduct(response):
    if response.method == "POST":
        form = AddProduct(response.POST, response.FILES)

        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["category"]
            b = form.cleaned_data["brand"]
            d = form.cleaned_data["description"]
            pr = form.cleaned_data["price"]
            pic = form.cleaned_data["product_img"]

            p = Product(name = n, category = c, brand = b, description = d, price = pr, product_img = pic)
            p.save()
            
        return HttpResponseRedirect("/products")
    
    else:
        form = AddProduct()

    return render(response, "main/addproduct.html", {"form":form})