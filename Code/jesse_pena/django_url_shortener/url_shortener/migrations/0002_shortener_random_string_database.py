# Generated by Django 3.1.2 on 2020-11-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortener',
            name='random_string_database',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
