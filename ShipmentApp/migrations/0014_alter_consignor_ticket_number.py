# Generated by Django 5.1.6 on 2025-02-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipmentApp', '0013_alter_consignor_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignor',
            name='ticket_number',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
