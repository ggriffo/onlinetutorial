# Generated by Django 2.0.5 on 2018-06-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='created_by',
            field=models.CharField(default='', max_length=200),
        ),
    ]
