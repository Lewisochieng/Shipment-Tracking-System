from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Shipment, Consignor

@receiver(post_save, sender=Shipment)
def activate_consignor_on_shipment(sender, instance, created, **kwargs):
    """
    Activate the consignor if a shipment is created or updated with quantity > 0.
    """
    if instance.quantity > 0:
        consignor = instance.consignor
        consignor.is_active = True
        consignor.save()

@receiver(post_delete, sender=Shipment)
def deactivate_consignor_if_no_shipments(sender, instance, **kwargs):
    """
    Deactivate the consignor if there are no shipments left with quantity > 0.
    """
    consignor = instance.consignor
    if not consignor.shipments.filter(quantity__gt=0).exists():
        consignor.is_active = False
        consignor.save()
