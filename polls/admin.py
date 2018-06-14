from django.contrib import admin

from .models import Choice, Question, Product, Store, Shopping, Customer, Sale, Order


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ['brand', 'name']
    list_display = ('name', 'brand', 'genre', 'has_image')

class StoreAdmin(admin.ModelAdmin):
    model = Store
    search_fields = ['name']

class ShoppingAdmin(admin.ModelAdmin):
    model = Shopping
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
    model = Product
    search_fields = ['order_when', 'total']
    list_display = ('order_when', 'total')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Shopping, ShoppingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Order, OrderAdmin)