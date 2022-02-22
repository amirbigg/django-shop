from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


class HomeView(View):
	def get(self, request):
		products = Product.objects.filter(available=True)
		return render(request, 'home/home.html', {'products':products})


class ProductDetailView(View):
	def get(self, request, slug):
		product = get_object_or_404(Product, slug=slug)
		return render(request, 'home/detail.html', {'product':product})