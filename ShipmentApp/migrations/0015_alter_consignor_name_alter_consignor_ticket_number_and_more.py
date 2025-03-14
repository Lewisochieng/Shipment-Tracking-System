# Generated by Django 5.1.6 on 2025-02-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShipmentApp', '0014_alter_consignor_ticket_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignor',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='consignor',
            name='ticket_number',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='ticket_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
