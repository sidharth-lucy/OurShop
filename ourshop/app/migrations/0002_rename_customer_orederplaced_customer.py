# Generated by Django 4.0.6 on 2022-07-30 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orederplaced',
            old_name='Customer',
            new_name='customer',
        ),
    ]