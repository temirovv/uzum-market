from django.urls import path
from .views import product_list, product_detail, add_to_cart, \
    user_cart, delete_cart_item_view, pochta_junat, ProductListView, ProductListTemplateView


urlpatterns = [
    # path('', ProductListView.as_view(), name='product_list'),
    path('', ProductListTemplateView.as_view(), name='product_list'),
    # path('', product_list, name='product_list'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('user-cart/', user_cart, name='user_cart'),
    path('delete-cart/', delete_cart_item_view, name='delete_cart_item_view'),
    path('pochta_junat', pochta_junat)
]
