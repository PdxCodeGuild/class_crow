# Generated by Django 3.1.2 on 2020-10-31 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20201031_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villain',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Movie', to='movies.movie'),
        ),
    ]
