from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# Automatically create a Profile when a User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name
        )


# Log profile save
@receiver(post_save, sender=Profile)
def profile_updated(sender, instance, created, **kwargs):
    print('Profile saved:', instance)
    print('Created:', created)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()