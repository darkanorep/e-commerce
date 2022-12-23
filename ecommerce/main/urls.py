from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("products/",views.products, name="products"),
    path("products/<int:id>",views.product, name="product"),
    path("products/create", views.addproduct, name="addproduct")
]