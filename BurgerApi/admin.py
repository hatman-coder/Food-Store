from django.contrib import admin
from BurgerApi.models import UserProfile, OrderDetail, OrderMaster, CustomerDetail, Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'in_stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


admin.site.register(UserProfile)
admin.site.register(CustomerDetail)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail)
admin.site.register(OrderMaster)
