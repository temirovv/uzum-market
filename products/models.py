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
    short_description = TextField()
    description = TextField()
    quantity = PositiveIntegerField(default=1)
    category = ForeignKey('products.Category', CASCADE, related_name='products')
    

    def __str__(self) -> str:
        return self.name

    @property
    def first_image(self):
        return self.images.all().first()

    @property
    def get_price(self):
        if self.discount:
            price = self.price - (self.price*self.discount)/100
            return price
        
        return self.price

class ProductImage(Model):
    image = ImageField(upload_to='products')
    product = ForeignKey('products.Product', CASCADE, related_name='images')


class Color(Model):
    name = CharField(max_length=20)
    product = ForeignKey('products.Product', CASCADE, related_name='colors')
