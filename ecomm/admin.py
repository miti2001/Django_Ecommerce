from django.contrib import admin
from .models import Order, Customer, OrderItem, ProductInformation, Feedback, ShippingAddress

# Register your models here.

admin.site.register(ProductInformation)
admin.site.register(Feedback)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
