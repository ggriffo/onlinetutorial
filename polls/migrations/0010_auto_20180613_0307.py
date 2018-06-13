# Generated by Django 2.0.5 on 2018-06-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('CATANDJACK', 'Cat and Jack'), ('CARTERS', 'Cat and Jack'), ('OSHKOSH', 'Oshkosh'), ('OSHKOSHG', 'Oshkosh Genuino'), ('CENTRUM', 'Centrum'), ('COLICCALM', 'Colic Calm'), ('DESISTIN', 'Desistin'), ('DISNEY', 'Disney'), ('GAP', 'GAP'), ('KIRKLAND', 'Kirkland'), ('NATROL', 'Natrol'), ('NATURESBOUNTY', 'Natures Bounty'), ('OTHERS', 'Others')], default='CATANDJACK', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], default='F', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('NB', 'New Born'), ('03M', '0-3 Months'), ('06M', '3-6 Months'), ('09M', '6-9 Months'), ('12M', '9-12 Months'), ('18M', '18 Months'), ('02T', '2 Years'), ('03T', '3 Years'), ('04T', '4 Years'), ('05T', '5 Years'), ('06T', '6 Years'), ('07T', '7 Years'), ('08T', '8 Years'), ('UNQ', 'Unique')], default='NB', max_length=3),
        ),
    ]
