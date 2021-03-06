# Generated by Django 2.0.6 on 2018-06-14 19:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20180614_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_when',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Ordered When'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_when',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Sold when'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='shopping_on',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Shopping on'),
        ),
    ]
