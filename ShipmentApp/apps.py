from django.apps import AppConfig


class ShipmentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ShipmentApp'

    def ready(self):
        import ShipmentApp.signals
