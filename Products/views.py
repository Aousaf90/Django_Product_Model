from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Products
# Create your views here.
def show_products(request):
    products = Products.objects.all()
    product_list = list(products.values())
    return JsonResponse({'Products': product_list}, safe=False)