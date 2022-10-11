from django.contrib import admin
from BurgerApi.models import UserProfile, Order, CustomerDetail, Category, Product


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'products', 'customer', 'orderTime')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'in_stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


admin.site.register(UserProfile)
admin.site.register(Order, OrderAdmin)
admin.site.register(CustomerDetail)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
