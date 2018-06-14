from django.contrib import admin

from .models import Product, Store, Shopping, Customer, Sale, Order, Brand, ShoppingProduct

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    model = Brand
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ['brand', 'name']
    list_display = ('name', 'brand', 'genre', 'has_image')

class StoreAdmin(admin.ModelAdmin):
    model = Store
    search_fields = ['name']

class ShoppingProductInLine(admin.TabularInline):
    model = ShoppingProduct
    readonly_fields = ('real_price',)
    extra = 3

class ProductInLine(admin.TabularInline):
    model = Product
    extra = 3

class ShoppingAdmin(admin.ModelAdmin):
    model = Shopping
    inlines = [ShoppingProductInLine]
    search_fields = ['store', 'shopping_on']
    list_display = ('store', 'shopping_on')

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    search_fields = ['name', 'street_address', 'city']
    list_display = ('name', 'street_address', 'city')

class SaleAdmin(admin.ModelAdmin):
    model = Sale
    search_fields = ['sold_when', 'total']
    list_display = ('sold_when', 'total')

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [ProductInLine]
    search_fields = ['order_when', 'total']
    list_display = ('order_when', 'total')

admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Shopping, ShoppingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brand, BrandAdmin)