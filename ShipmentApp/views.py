from django.shortcuts import render, redirect, get_object_or_404
from ShipmentApp.models import Consignor, Consignee, Shipment
from .forms import ConsignorForm, ConsigneeForm, ShipmentForm
from django.contrib import messages
from django.http import HttpResponse


def consignor_list(request):
    consignors = Consignor.objects.all()
    return render(request, 'consignor_list.html', {'consignors': consignors})

def consignor_add(request):
    if request.method == 'POST':
        if len(request.POST.get('name', '')) > 100:
            return HttpResponse("Error: Name is too long", status=400)
        form = ConsignorForm(request.POST)
        if form.is_valid():
            consignor = form.save(commit=False)
            consignor.is_active = False  # Ensure new consignor is archived
            consignor.save()
            return redirect('archived_consignors')  # Redirect to archived list
    else:
        form = ConsignorForm()
    return render(request, 'consignor_form.html', {'form': form})


def consignor_edit(request, pk):
    consignor = get_object_or_404(Consignor, pk=pk)
    if request.method == 'POST':
        form = ConsignorForm(request.POST, instance=consignor)
        if form.is_valid():
            form.save()
            return redirect('consignor_list')
    else:
        form = ConsignorForm(instance=consignor)
    return render(request, 'consignor_form.html', {'form': form})


def consignor_delete(request, pk):
    consignor = get_object_or_404(Consignor, pk=pk)

    # Prevent deletion of active consignors
    if consignor.is_active:
        messages.error(request, "Cannot delete an active consignor. Archive the consignor first.")
        return redirect('consignor_list')

    # Delete the consignor if archived
    consignor.delete()
    messages.success(request, "Consignor deleted successfully.")
    return redirect('consignor_list')

def shipment_list(request):
    shipments = Shipment.objects.all().order_by('ticket_number')
    return render(request, 'shipment_list.html', {'shipments': shipments})

def shipment_add(request):
    if request.method == 'POST':
        if len(request.POST.get('name', '')) > 50:
            return HttpResponse("Error: Name is too long", status=400)
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = ShipmentForm()
        print("Rendering template: shipment_form.html")  # Debugging
    return render(request, 'shipment_form.html', {'form': form})

def shipment_edit(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'shipment_form.html', {'form': form})


def shipment_delete(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)

    try:
        shipment.delete()
        messages.success(request, "Shipment deleted successfully.")
    except ValueError as e:
        messages.error(request, str(e))

    return redirect('shipment_list')

def home(request):
    return render(request, 'home.html')

def active_consignors(request):
    # Fetch active consignors (is_active=True)
    active_consignors = Consignor.objects.filter(is_active=True)
    return render(request, 'active_consignors.html', {'active_consignors': active_consignors})

def archived_consignors(request):
    # Fetch archived consignors (is_active=False)
    archived_consignors = Consignor.objects.filter(is_active=False)
    return render(request, 'archived_consignors.html', {'archived_consignors': archived_consignors})


def delete_archived_consignor(request, pk):
    consignor = get_object_or_404(Consignor, pk=pk)

    if not consignor.is_active:  # Ensure it's archived before deleting
        consignor.delete()
        messages.success(request, "Archived consignor deleted successfully.")
    else:
        messages.error(request, "This consignor is active and cannot be deleted.")

    return redirect('archived_consignors')

