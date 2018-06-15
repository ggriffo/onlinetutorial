from django.contrib import admin

from django.utils import timezone
from django import forms
from datetime import datetime
from .models import Product, Store, Shopping, Customer, Order, Brand, OrderItem, ShoppingProduct, OrderPayment

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
    extra = 1

class ShoppingAdmin(admin.ModelAdmin):
    model = Shopping
    inlines = [ShoppingProductInLine]
    search_fields = ['store', 'shopping_on']
    list_display = ('store', 'shopping_on')

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    search_fields = ['name', 'street_address', 'city']
    list_display = ('name', 'street_address', 'city')

class OrderItemFormset(forms.models.BaseInlineFormSet):
    def is_valid(self):
        return super(OrderItemFormset, self).is_valid() and \
                    not any([bool(e) for e in self.errors])

    def clean(self):
        for form in self.forms:
            delivered_date = form.cleaned_data['delivered_date']
            current_date = datetime.date(timezone.now())
            if (delivered_date):
                if (delivered_date > current_date):
                    raise forms.ValidationError(('Delivered date cannot be greater than today.'), code='invalid')

class OrderPaymentFormset(forms.models.BaseInlineFormSet):
    def is_valid(self):
        return super(OrderPaymentFormset, self).is_valid() and \
                    not any([bool(e) for e in self.errors])
    
    def clean(self):
        for form in self.forms:
            payment_date = form.cleaned_data['payment_date']
            current_date = datetime.date(timezone.now())
            if (payment_date):
                if (payment_date > current_date):
                    raise forms.ValidationError(('Payment date cannot be greater than today.'), code='invalid')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    formset = OrderItemFormset
    readonly_fields = ('item_price',)
    extra=0

class OrderPaymentInLine(admin.TabularInline):
    model = OrderPayment
    formset = OrderPaymentFormset
    extra=0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderItemInline, OrderPaymentInLine]
    readonly_fields = ('order_total', 'total_paid', 'payment_status', 'delivery_status')
    search_fields = ['order_to', 'order_when', 'order_total']
    list_display = ('order_to', 'order_when', 'order_total', 'order_sold', 'sold_when')

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shopping, ShoppingAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Brand, BrandAdmin)