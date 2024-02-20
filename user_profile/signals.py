from django.db.models.signals import post_save
from custom_user.models import User
from django.dispatch import receiver
from .models import Profile


# Creating profile for a new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Saving profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
