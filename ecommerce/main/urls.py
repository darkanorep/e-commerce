from django.urls import path
from . import views, cart, review, checkout

urlpatterns = [
    path("",views.index, name="index"),
    path("products/",views.products, name="products"),
    path("products/<str:gender>",views.gender_products, name="product_gender"),
    path("products/<str:gender>/<str:category>",views.categorize_products, name="product_categorize"),
    path("products/<str:gender>/<str:category>/<int:id>",views.specific_products, name="specific_product"),
    path("products/create", views.addproduct, name="addproduct"),
    path("config/", views.stripe_config, name="stripe_config"),
    path("cart", views.mycart, name="cart"),
    path("addtocart", cart.addtocart, name="addtocart"),
    path("updatecart", cart.updatecart, name="updatecart"),
    path("cart/remove/<int:id>", cart.removeitem, name="removeitem"),
    path("addreview", review.addreview, name="addreview"),
    path('create_checkout_session/', checkout.create_checkout_session, name='checkout'),
    path('buy_now/', checkout.buy_now, name='buy_now')
    
]