from django.contrib import admin
from .models import Customer, Product, Order, OrderItem

# Register your models here.
admin.site.register([Customer, Product, Order, OrderItem])