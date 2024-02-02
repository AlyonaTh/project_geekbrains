from django.shortcuts import render
from django.views.generic.base import View
from .models import Product


class ShopView(View):
    """Products"""
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        return render(request, 'shop.html', {'product_list': products})