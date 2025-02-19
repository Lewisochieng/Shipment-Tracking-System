from django.db import models
import uuid

class Consignor(models.Model):
    name = models.CharField(max_length=50)
    ticket_number = models.CharField(max_length=50, unique=True, blank=True)  # Unique ticket number
    is_active = models.BooleanField(default=False)
    total_quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.ticket_number})"

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = self.generate_ticket_number()
        super().save(*args, **kwargs)

    def generate_ticket_number(self):
        """ Generate a unique ticket number """
        while True:
            ticket_number = f"CONS-{uuid.uuid4().hex[:6].upper()}"
            if not Consignor.objects.filter(ticket_number=ticket_number).exists():
                return ticket_number



class Consignee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('warehouse', 'In Warehouse'),
        ('transit', 'In Transit'),
    ]

    consignor = models.ForeignKey(Consignor, on_delete=models.CASCADE, related_name="shipments")
    consignee = models.ForeignKey(Consignee, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=50, blank=True)  # Inherit from Consignor
    goods_description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    shipment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='warehouse')

    def save(self, *args, **kwargs):
        """ Assign the same ticket number as the consignor """
        if not self.ticket_number:
            self.ticket_number = self.consignor.ticket_number

        # Update shipment status
        self.status = 'warehouse' if self.quantity > 0 else 'transit'

        # Update consignor's total quantity
        if self.pk:  # Updating an existing shipment
            old_shipment = Shipment.objects.get(pk=self.pk)
            quantity_difference = self.quantity - old_shipment.quantity
        else:  # Creating a new shipment
            quantity_difference = self.quantity

        self.consignor.total_quantity += quantity_difference
        self.consignor.is_active = self.consignor.total_quantity > 0
        self.consignor.save()

        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        # Prevent deletion if the consignor is active
        if self.consignor.is_active:
            raise ValueError("Cannot delete a shipment associated with an active consignor.")

        # Update consignor's total quantity when a shipment is deleted
        self.consignor.total_quantity -= self.quantity
        self.consignor.save()
        super().delete(*args, **kwargs)

