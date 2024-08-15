from django.db.models import (
    Model,
    CharField, ForeignKey, 
    CASCADE, ImageField,
    PositiveIntegerField, FloatField,
    TextField
    )


class Category(Model):
    name = CharField(max_length=120)
    parent = ForeignKey('self', CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Product(Model):
    name = CharField(max_length=1000)
    price = FloatField()
    discount = PositiveIntegerField()
    color = CharField(max_length=30, null=True, blank=True)
    short_description = TextField()
    description = TextField()
    quantity = PositiveIntegerField(default=1)
    category = ForeignKey('products.Category', CASCADE, related_name='products')
    
    def __str__(self) -> str:
        return self.name

class ProductImage(Model):
    image = ImageField(upload_to='products')
    product = ForeignKey('products.Product', CASCADE, related_name='images')
