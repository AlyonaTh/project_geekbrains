from django.shortcuts import render
from django.views.generic.base import View
from .models import About
from blogapp.models import Post
from shop.models import Product


class AboutView(View):
    """About View"""
    def get(self, request):
        about = About.objects.all()
        return render(request, 'about.html', {'about': about})


class IndexView(View):
    """Index View"""
    def get(self, request):
        posts = Post.objects.all().order_by('-id')[:4]
        products = Product.objects.all().order_by('-id')[:6]
        return render(request, 'index.html', {'post_list': posts, 'product_list': products})