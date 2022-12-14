from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


class Forum(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.TextField(max_length=255)
    body = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
