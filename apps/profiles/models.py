from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'), related_name='profile')

    def __unicode__(self):
        return self.user.username


@receiver(models.signals.post_save, sender=get_user_model())
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
