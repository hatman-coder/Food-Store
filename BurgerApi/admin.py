from django.contrib import admin
from BurgerApi.models import UserProfile, Order, AddOnes, CustomerDetail, Category, Product


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'products', 'customer', 'orderTime')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'in_stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(AddOnes)
admin.site.register(CustomerDetail)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
