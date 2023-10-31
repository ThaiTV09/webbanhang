from django.contrib import admin
from .models import *

# đăng ký 5 class đã đăng ký trong model.py.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)