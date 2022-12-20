from multiprocessing.reduction import register
from django.contrib import admin
from .models import Product, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)