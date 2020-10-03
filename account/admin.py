from django.contrib import admin
from .models import ExtendedUser, Order, payment

# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(Order)
admin.site.register(payment)

