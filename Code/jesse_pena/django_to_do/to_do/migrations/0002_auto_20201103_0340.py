# Generated by Django 3.1.2 on 2020-11-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='to_do_item',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
