from django.shortcuts import render, redirect

# Create your views here.
from django.http.response import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import Product, Cart
from .forms import AddProduct, AddReview
from .cart import removeitem

def index(response):
    return render(response, "main/index.html")

def products(response):
    p = Product.objects.all()
    return render(response, "main/products.html", {"p":p})

def product(response, id):
    p = Product.objects.get(id=id)
    form = AddReview()
    return render(response, "main/product.html", {"p":p, "form":form})

def mycart(response):
    if response.user.is_authenticated == True:
        cart = Cart.objects.filter(user = response.user)

        return render(response, "main/cart.html", ({"cart": cart}))

    return render(response, "main/cart.html")

# def removefromcart(response, id):
#     Cart.objects.filter(id=id).delete()

#     return redirect("/cart")
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

