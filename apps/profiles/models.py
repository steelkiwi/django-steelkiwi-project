from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'), related_name='profile')

    def __unicode__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
