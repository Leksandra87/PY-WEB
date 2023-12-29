from django.urls import path

from .views import CartView, ProductView, ShopView

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('product/', ProductView.as_view()),
    path('shop/', ShopView.as_view()),
]
