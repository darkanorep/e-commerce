from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponseRedirect, HttpResponse
from .models import Product, Review
from .forms import AddReview

def addreview(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            product_id = int(response.POST.get("product_id"))
            comment = response.POST.get("comment")
            review_img = response.FILES.get('review_img')
        
            try:
                Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse({"status": "No such Product found"})

            if Review.objects.filter(user=response.user.id, product_id=product_id).exists():
                return JsonResponse({"status": "Already Reviewed"})

            Review.objects.create(user=response.user, product_id=product_id, comment=comment, review_img=review_img)
            return JsonResponse({"status": "Successfully Added"})
            
        return redirect("/")
    
    return redirect("/")