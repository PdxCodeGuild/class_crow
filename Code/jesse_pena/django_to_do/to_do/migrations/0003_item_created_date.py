# Generated by Django 3.1.2 on 2020-11-03 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0002_auto_20201103_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]