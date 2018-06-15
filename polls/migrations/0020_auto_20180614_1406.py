# Generated by Django 2.0.6 on 2018-06-14 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20180614_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_when',
            field=models.DateField(default=datetime.datetime(2018, 6, 14, 19, 6, 2, 590843, tzinfo=utc), verbose_name='Ordered When'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_when',
            field=models.DateField(default=datetime.datetime(2018, 6, 14, 19, 6, 2, 590843, tzinfo=utc), verbose_name='Sold when'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='shopping_on',
            field=models.DateField(default=datetime.datetime(2018, 6, 14, 19, 6, 2, 590843, tzinfo=utc), verbose_name='Shopping on'),
        ),
    ]