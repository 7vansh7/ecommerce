from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)