from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Counter

@receiver(post_save, sender=User)
def create_save_counter(sender, created, instance, **kwargs):
    if created:
        counter = Counter.objects.create(user = instance)
        counter.save()
