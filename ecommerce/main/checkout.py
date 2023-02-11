from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from main.models import Product, Cart
import stripe

def create_checkout_session(response):
    if response.method == 'GET':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price = Product.objects.values('stripe_id')
        quantity = Cart.objects.values('quantity')

        item = []
        
        for price, quantity in zip(price, quantity):
            item.append({**price, **quantity})
        
        item_list = []

        for items in item:
            price = items.pop('stripe_id')
            items['price'] = price
            item_list.append(items)

        try:
            checkout_session = stripe.checkout.Session.create(
                shipping_address_collection={"allowed_countries": ["PH"]},
                shipping_options=[
                    {
                    "shipping_rate_data": {
                        "type": "fixed_amount",
                        "fixed_amount": {"amount": 6000, "currency": "php"},
                        "display_name": "Shipping Days",
                        "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 5},
                        "maximum": {"unit": "business_day", "value": 7},
                        },
                    },
                    },
                ],
                line_items=item_list,
                mode='payment',
                success_url='http://127.0.0.1:8000/cart',
                cancel_url='http://127.0.0.1:8000/cart',
            )
            Cart.objects.filter(user = response.user).delete()
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return str(e)

    return redirect(checkout_session.url, code=303)

