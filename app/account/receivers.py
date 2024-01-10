from django.db.models.signals import pre_save
from django.dispatch import receiver

from account.models import User


@receiver(pre_save, sender=User)
def lower_user_email(instance, **kwargs):
    instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def save_user_phone_number(sender, instance, **kwargs):
    if instance.phone_number:
        instance.phone_number = ''.join(filter(str.isdigit, instance.phone_number))
