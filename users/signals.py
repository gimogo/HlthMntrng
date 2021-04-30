from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver
from .models import Patient, Doctor

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
    if created and instance.is_patient:
        Patient.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created and instance.is_doctor:
        Doctor.objects.create(user=instance)
