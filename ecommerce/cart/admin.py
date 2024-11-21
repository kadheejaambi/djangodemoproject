from django.contrib import admin

# Register your models here.
from cart.models import Cart,Order_detail,Payment
admin.site.register(Cart)
admin.site.register(Order_detail)
admin.site.register(Payment)
