from django.contrib import admin
from .models import Allergen, Product, Order, OrderItem

admin.site.register(Allergen)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)