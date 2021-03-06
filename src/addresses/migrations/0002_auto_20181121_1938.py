# Generated by Django 2.1.2 on 2018-11-21 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='United States of America', max_length=120),
        ),
    ]
