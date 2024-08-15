from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import Category, Product, ProductImage


class ProductImageStackedInline(StackedInline):
    model = ProductImage
    fields = 'image', 'product'


