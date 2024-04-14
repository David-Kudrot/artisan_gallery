# Generated by Django 5.0.4 on 2024-04-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0002_rename_categroy_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
