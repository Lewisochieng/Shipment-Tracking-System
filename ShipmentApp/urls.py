from django.conf.urls.static import static
from django.urls import path
from ShipmentApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('active-consignors/', views.consignor_list, name='consignor_list'),
    path('consignors/add/', views.consignor_add, name='consignor_add'),
    path('consignors/edit/<int:pk>/', views.consignor_edit, name='consignor_edit'),
    path('consignors/delete/<int:pk>/', views.consignor_delete, name='consignor_delete'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('shipments/add/', views.shipment_add, name='shipment_add'),
    path('shipments/edit/<int:pk>/', views.shipment_edit, name='shipment_edit'),
    path('shipments/delete/<int:pk>/', views.shipment_delete, name='shipment_delete'),
    path('consignors/', views.active_consignors, name='active_consignors'),
    path('archived-consignors/', views.archived_consignors, name='archived_consignors'),
    path('archived-consignors/delete/<int:pk>/', views.delete_archived_consignor, name='delete_archived_consignor'),

]