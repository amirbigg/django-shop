from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
	sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
	is_sub = models.BooleanField(default=False)
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home:category_filter', args=[self.slug,])


class Product(models.Model):
	category = models.ManyToManyField(Category, related_name='products')
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	image = models.ImageField()
	description = RichTextField()
	price = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home:product_detail', args=[self.slug,])
