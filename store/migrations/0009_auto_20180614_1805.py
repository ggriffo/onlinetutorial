# Generated by Django 2.0.6 on 2018-06-14 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20180614_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shopping_product',
        ),
        migrations.AddField(
            model_name='shoppingproduct',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
            preserve_default=False,
        ),
    ]
