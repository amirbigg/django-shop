from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from . import tasks
from django.contrib import messages


class HomeView(View):
	def get(self, request):
		products = Product.objects.filter(available=True)
		return render(request, 'home/home.html', {'products':products})


class ProductDetailView(View):
	def get(self, request, slug):
		product = get_object_or_404(Product, slug=slug)
		return render(request, 'home/detail.html', {'product':product})


class BucketHome(View):
	template_name = 'home/bucket.html'

	def get(self, request):
		objects = tasks.all_bucket_objects_task()
		return render(request, self.template_name, {'objects':objects})


class DeleteBucketObject(View):
	def get(self, request, key):
		tasks.delete_object_task.delay(key)
		messages.success(request, 'your object will be delete soon.', 'info')
		return redirect('home:bucket')


class DownloadBucketObject(View):
	def get(self, request, key):
		tasks.download_object_task.delay(key)
		messages.success(request, 'your download will start soon.', 'info')
		return redirect('home:bucket')
