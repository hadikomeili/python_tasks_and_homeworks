# Generated by Django 3.2.5 on 2021-07-30 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe5', '0015_alter_receipts_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipts',
            name='time_stamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 30, 18, 17, 11, 105234)),
        ),
    ]
