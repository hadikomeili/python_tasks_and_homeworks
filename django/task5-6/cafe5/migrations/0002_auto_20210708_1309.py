# Generated by Django 3.2.5 on 2021-07-08 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='time_stamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 8, 13, 9, 14, 330662)),
        ),
        migrations.AlterField(
            model_name='receipts',
            name='time_stamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 8, 13, 9, 14, 331168)),
        ),
    ]