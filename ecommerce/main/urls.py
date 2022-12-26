from django.urls import path
from . import views, cart

urlpatterns = [
    path("",views.index, name="index"),
    path("products/",views.products, name="products"),
    path("products/<int:id>",views.product, name="product"),
    path("products/create", views.addproduct, name="addproduct"),
    path("addtocart", cart.addtocart, name="addtocart"),
    path("cart", views.mycart, name="cart")
]