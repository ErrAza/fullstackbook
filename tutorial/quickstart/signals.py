from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Employee


@receiver(post_save, sender=Employee)
def on_employee_save(sender, instance, **kwargs):
    print(str(instance) + " was saved!")


@receiver(pre_save, sender=Employee)
def on_employee_pre_save(sender, instance, **kwargs):
    print(str(instance) + " is about to be saved!")