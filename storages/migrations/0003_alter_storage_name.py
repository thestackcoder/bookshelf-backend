# Generated by Django 3.2.6 on 2021-08-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storages', '0002_rename_shelf_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
