# Generated by Django 2.0.5 on 2018-06-14 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20180614_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='dolar_price',
            new_name='dolarprice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='real_price',
            new_name='realprice',
        ),
    ]
