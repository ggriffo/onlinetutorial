# Generated by Django 2.0.6 on 2018-06-14 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180614_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingproduct',
            name='real_price',
        ),
    ]
