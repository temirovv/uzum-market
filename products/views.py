import json

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Product, Cart, CartItem


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


def add_to_cart(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        product = get_object_or_404(Product, id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    return JsonResponse(data={'status':'okey'})
