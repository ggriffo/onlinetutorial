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
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	photo = models.ImageField('Product Picture', blank=True)
	dolarprice = models.FloatField('Dolar Price')
	realprice = models.FloatField('Real Price')
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