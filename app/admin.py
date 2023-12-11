from django.contrib import admin
from .models import Manager, Product, Order


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'is_stuff')
    list_filter = ('fullname',)


admin.site.register(Manager, ManagerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', )
    list_filter = ('product_name',)


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('is_solved',)


admin.site.register(Order, OrderAdmin)
