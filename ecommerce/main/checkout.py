from django.conf import settings
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from main.models import Product, Cart
import stripe, json



def create_checkout_session(response):
    if response.method == 'GET':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        carts = Cart.objects.filter(user = response.user)
        
        item_list = []
        for cart in carts:
            product = Product.objects.get(id=cart.product.id)
            item_list.append({
                'price': product.stripe_id,
                'quantity': cart.quantity
            })

        try:
            checkout_session = stripe.checkout.Session.create(
                shipping_address_collection={"allowed_countries": ["PH"]},
                shipping_options=[
                    {
                    "shipping_rate_data": {
                        "type": "fixed_amount",
                        "fixed_amount": {"amount": 0, "currency": "php"},
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
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return str(e)

    return redirect(checkout_session.url, code=303)

def buy_now(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prod_id = data['id']
            price = data['price']
            quantity = data['quantity']
            print(prod_id)

            stripe.api_key = settings.STRIPE_SECRET_KEY
            checkout_session = stripe.checkout.Session.create(
                shipping_address_collection={"allowed_countries": ["PH"]},
                shipping_options=[
                    {
                    "shipping_rate_data": {
                        "type": "fixed_amount",
                        "fixed_amount": {"amount": 0, "currency": "php"},
                        "display_name": "Shipping Days",
                        "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 5},
                        "maximum": {"unit": "business_day", "value": 7},
                        },
                    },
                    },
                ],
                line_items=[
                    {
                        'price': price,
                        'quantity': quantity
                    }
                ],
                mode='payment',
                success_url='http://127.0.0.1:8000/cart',
                cancel_url=f'http://127.0.0.1:8000/products/{prod_id}',
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return HttpResponseBadRequest(str(e))

    return HttpResponseBadRequest('Invalid request method')