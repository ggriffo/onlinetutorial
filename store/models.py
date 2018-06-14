from django.db import models

from django.utils import timezone
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField('Name', max_length=50)
    street_address = models.CharField('Street', max_length=50, blank=True)
    city = models.CharField('City', max_length=50, blank=True)
    details = models.CharField('Details', max_length=300, blank=True)
    def __str__(self):
        return self.name
        
class Store(models.Model):
    name = models.CharField('Store', max_length=100)
    def __str__(self):
        return self.name

class Shopping(models.Model):
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    shopping_on = models.DateField('Shopping on', default=timezone.now)
    dolar_quotation = models.DecimalField('Dolar Quotation', max_digits=5, decimal_places=2)
    #def __str__(self):
        #return self.shopping_on
        
class Order(models.Model):
    order_to = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_when = models.DateField('Ordered When', default=timezone.now)
    total = models.DecimalField('Order Total', default=0, max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.order_to.name

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField('Product Picture', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    GENRE = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    genre = models.CharField(max_length=2,
        choices=GENRE,
        default='F')

    def __str__(self):
        return self.name
    def has_image(self):
        return self.photo

class ShoppingProduct(models.Model):
    shopping = models.ForeignKey(Shopping, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    dolar_price = models.DecimalField('Dolar Price', max_digits=6, decimal_places=2)
    real_price = models.DecimalField('Real Price', max_digits=6, decimal_places=2)
    sales_price = models.DecimalField('Sales Price', max_digits=6, decimal_places=2)
    quantity = models.IntegerField('Quantity')
    SIZES = (
        ('NB', 'New Born'),
        ('03M', '0-3 Months'),
        ('06M', '3-6 Months'),
        ('09M', '6-9 Months'),
        ('12M', '9-12 Months'),
        ('18M', '18 Months'),
        ('02T', '2 Years'),
        ('03T', '3 Years'),
        ('04T', '4 Years'),
        ('05T', '5 Years'),
        ('06T', '6 Years'),
        ('07T', '7 Years'),
        ('08T', '8 Years'),
        ('UNQ', 'Unique'),
    )
    size = models.CharField(max_length=3,
        choices=SIZES,
        default='NB')
    
    def __str__(self):
        return self.product.name
    
    def save(self):
        self.real_price = self.dolar_price * self.shopping.dolar_quotation
        super(ShoppingProduct, self).save()

class Sale(models.Model):
    sold_to = models.ForeignKey(Customer, on_delete=models.PROTECT)
    sold_when = models.DateField('Sold when', default=timezone.now)
    shopping_product = models.ForeignKey(ShoppingProduct, on_delete=models.PROTECT)
    total = models.DecimalField('Sale Total', default=0, max_digits=6, decimal_places=2)
    def __str__(self):
        return self.sold_to