import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/product-list.html', context=context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'products/product-detail.html', context=context)


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)


    return JsonResponse(data={'status':'okey'})
