from django.shortcuts import render
from django.views import View


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ProductView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')


class ShopView(View):
    def get(self, request):
        context = {'data': [{'name': 'Bell Pepper',
                             'discount': 30,
                             'price_before': 120.00,
                             'price_after': 80.00,
                             'url': 'store/images/product-1.jpg'}
                            ]
                   }

        return render(request, 'store/shop.html', context)

# Create your views here.
