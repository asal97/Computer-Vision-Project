from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class SystemUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=30, blank=True)
    nationalCode = models.CharField(max_length=10)
    approved = models.BooleanField(default=False)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        SystemUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
