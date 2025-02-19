
from django.contrib import admin
from .models import Consignee, Consignor, Shipment

admin.site.register(Consignee)
admin.site.register(Consignor)
admin.site.register(Shipment)