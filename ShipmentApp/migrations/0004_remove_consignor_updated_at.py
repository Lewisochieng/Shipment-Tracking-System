# Generated by Django 5.1.3 on 2025-02-17 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShipmentApp', '0003_consignor_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consignor',
            name='updated_at',
        ),
    ]
