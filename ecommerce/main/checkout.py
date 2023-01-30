from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from main.models import Product, Cart
from django.views.decorators.csrf import csrf_exempt
import stripe

@csrf_exempt
def create_checkout_session(response):
    if response.method == 'GET':
        domain_url = 'http://127.0.0.1:8000'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1MVsmDEoOM2qSKyAsDp9twaN',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://google.com',
                cancel_url='http://google.com',
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return str(e)

    return redirect(checkout_session.url, code=303)

