from django.urls import path

from .views import CartView, ProductView, ShopView

app_name = 'store'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('', ShopView.as_view(), name='shop'),
]
