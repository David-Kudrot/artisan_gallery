# Generated by Django 5.0.4 on 2024-04-14 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categroy',
            new_name='Category',
        ),
    ]