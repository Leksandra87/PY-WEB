from django.urls import path
from rest_framework import routers
from .views import CartView, ProductView, ShopView, CartViewSet

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)


app_name = 'store'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductView.as_view(), name='product'),
    path('', ShopView.as_view(), name='shop'),
]

