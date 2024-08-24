from django.contrib.admin import ModelAdmin, register, StackedInline

from .models import (
    Category, Product, ProductImage, 
    Color, Cart, CartItem, Order, OrderItem)


class ProductImageStackedInline(StackedInline):
    model = ProductImage
    fields = 'image', 'product'


class ColorStackedInline(StackedInline):
    model = Color
    fields = 'name', 'product'


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ProductImageStackedInline, ColorStackedInline
    list_display = 'name', 'category', 'price', 'quantity'


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@register(Cart)
class CartModelAdmin(ModelAdmin):
    pass


@register(CartItem)
class CartItemModelAdmin(ModelAdmin):
    pass


@register(Order)
class OrderModelAdmin(ModelAdmin):
    pass

@register(OrderItem)
class OrderItemModelAdmin(ModelAdmin):
    pass
