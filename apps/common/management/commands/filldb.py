import sys

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from profiles.factories import AdminFactory


class Command(BaseCommand):
    help = 'Fill the database with test fixtures'

    def handle(self, *args, **options):
        sys.stdout.write('Starting fill db\r\n')

        site = Site.objects.get(pk=1)
        site.domain = site.name = settings.DOMAIN
        site.save()

        AdminFactory()

        sys.stdout.write('Completed fill db\r\n')
