# Generated by Django 3.1.2 on 2020-10-31 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='villain',
            name='image',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]