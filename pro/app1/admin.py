from django.contrib import admin
from .models import Register
from . models import Cart

from .models import Product
from .models import OrderItem
from .models import Order

admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
# Register your models here.
class registeradmin(admin.ModelAdmin):
    list_display=('name','gender','address','phone')
admin.site.register(Register,registeradmin)



