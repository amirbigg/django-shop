from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ('category',)