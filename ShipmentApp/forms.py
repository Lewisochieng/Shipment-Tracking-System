
from django import forms
from .models import Consignor, Consignee, Shipment

class ConsignorForm(forms.ModelForm):
    class Meta:
        model = Consignor
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': '50'})  # Matches new model limit
        }


class ConsigneeForm(forms.ModelForm):
    class Meta:
        model = Consignee
        fields = ['name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': '50'}), # Matches new model limit
            'address': forms.TextInput(attrs={'maxlength': '50'})
        }

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['consignor', 'consignee', 'goods_description', 'quantity']
        widgets = {
            'goods_description': forms.TextInput(attrs={'maxlength': '100'}), # Matches new model limit
            'quantity': forms.NumberInput(attrs={'maxlength': '10000000'})  # Matches new model limit
        }