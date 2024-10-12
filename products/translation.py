from modeltranslation.translator import translator, TranslationOptions, register
from .models import Product, Category

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = 'name',

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = 'name', 'short_description', 'description'



# translator.register(Product, ProductTranslationOptions)
# translator.register(Category, CategoryTranslationOptions)