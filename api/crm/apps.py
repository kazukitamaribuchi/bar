from django.apps import AppConfig


class CrmConfig(AppConfig):
    name = 'crm'

    def ready(self):
        try:
            from .signals import (
                sales_detail_receiver,
            )
        except ImportError:
            pass
