from django.contrib import admin
from . models import Order

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    fields=('id','contact','address','address_description','order_amount','isComplete')
    date_hierarchy='created_at'
