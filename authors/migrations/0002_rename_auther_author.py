# Generated by Django 3.2.6 on 2021-08-22 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auther',
            new_name='Author',
        ),
    ]