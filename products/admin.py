from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import Category, Product, ProductImage


class ProductImageStackedInline(StackedInline):
    model = ProductImage
    fields = 'image', 'product'


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ProductImageStackedInline, 
    list_display = 'name', 'category', 'price', 'quantity'


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass
