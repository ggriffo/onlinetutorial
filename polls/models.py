import datetime

from django.utils import timezone
from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Product(models.Model):
	display_on_store = models.BooleanField('Display product on store', default=True)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	photo = models.ImageField('Product Picture', blank=True)

	BRANDS = (
		('CATANDJACK', 'Cat and Jack'),
		('CARTERS', 'Carters'),
		('OSHKOSH', 'Oshkosh'),
		('OSHKOSHG', 'Oshkosh Genuino'),
		('CENTRUM', 'Centrum'),
		('COLICCALM', 'Colic Calm'),
		('DESISTIN', 'Desistin'),
		('DISNEY', 'Disney'),
		('GAP', 'GAP'),
		('KIRKLAND', 'Kirkland'),
		('NATROL', 'Natrol'),
		('NATURESBOUNTY', 'Natures Bounty'),
		('OTHERS', 'Others'),
	)
	brand = models.CharField(max_length=15,
		choices=BRANDS,
		default='CATANDJACK')

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

class Store(models.Model):
	name = models.CharField('Store', max_length=100)
	def __str__(self):
		return self.name

class ShoppingProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.PROTECT)
	dolar_price = models.DecimalField('Dolar Price', default=0, max_digits=6, decimal_places=2)
	dolar_quotation = models.DecimalField('Dolar Quotation', default=0, max_digits=5, decimal_places=2)
	real_price = models.DecimalField('Real Price', default=0, max_digits=6, decimal_places=2)
	sales_price = models.DecimalField('Sales Price', default=0, max_digits=6, decimal_places=2)
	quantity = models.IntegerField('Quantity', default=1)
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

class Shopping(models.Model):
	store = models.ForeignKey(Store, on_delete=models.PROTECT)
	shopping_on = models.DateField('Shopping on', default=timezone.now())
	shopping_product = models.ForeignKey(ShoppingProduct, on_delete=models.PROTECT)
	def __str__(self):
    		return self.shopping_on

class Customer(models.Model):
	name = models.CharField('Name', max_length=50)
	street_address = models.CharField('Street', max_length=50, blank=True)
	city = models.CharField('City', max_length=50, blank=True)
	details = models.CharField('Details', max_length=300, blank=True)
	def __str__(self):
		return self.name

class Sale(models.Model):
	sold_to = models.ForeignKey(Customer, on_delete=models.PROTECT)
	sold_when = models.DateField('Sold when', default=timezone.now())
	shopping_product = models.ForeignKey(ShoppingProduct, on_delete=models.PROTECT)
	total = models.DecimalField('Sale Total', default=0, max_digits=6, decimal_places=2)
	def __str__(self):
    		return self.sold_to

class Order(models.Model):
	order_to = models.ForeignKey(Customer, on_delete=models.PROTECT)
	order_when = models.DateField('Ordered When', default=timezone.now())
	shopping_product = models.ForeignKey(ShoppingProduct, on_delete=models.PROTECT)
	total = models.DecimalField('Order Total', default=0, max_digits=6, decimal_places=2)
	def __str__(self):
		return self.order_to