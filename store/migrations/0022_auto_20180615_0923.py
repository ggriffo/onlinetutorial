# Generated by Django 2.0.6 on 2018-06-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20180615_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpayment',
            name='delivery_status',
        ),
        migrations.RemoveField(
            model_name='orderpayment',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(choices=[('ND', 'Not delivered'), ('PD', 'Partial Delivered'), ('TD', 'Total Delivered')], default='ND', max_length=4),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('NP', 'Not paid'), ('PP', 'Partial Paid'), ('TP', 'Total Paid')], default='NP', max_length=4),
        ),
    ]