from django.db.models import signals
from django.dispatch import receiver

from . import models

from formaloo.customers.customer import Customer


@receiver(signals.post_save, sender=models.ProjectUser)
def signal_post_save_user(sender, instance, created, **kwargs):
    if not instance.formaloo_customer_slug:
        customer = Customer(
            base_data={
                'code': instance.id
            }
        )
        customer.create()
