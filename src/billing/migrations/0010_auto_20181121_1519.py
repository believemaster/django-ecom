# Generated by Django 2.1.2 on 2018-11-21 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0009_charge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charge',
            old_name='refund',
            new_name='refunded',
        ),
    ]
