# Generated by Django 3.2.5 on 2021-07-29 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe5', '0012_auto_20210722_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipts',
            name='time_stamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 29, 7, 48, 33, 62631)),
        ),
    ]
