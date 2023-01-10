from django.contrib import admin
from BurgerApi.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'in_stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


class OrderMasterAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_time')


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'quantity')


admin.site.register(UserProfile)
admin.site.register(CustomerDetail)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(OrderMaster, OrderMasterAdmin)
admin.site.register(UserType)
admin.site.register(AddOns)
admin.site.register(PaymentType)
admin.site.register(OrderStatus)
