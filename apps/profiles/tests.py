from django.core.urlresolvers import reverse
from django.test import TestCase

from .factories import UserFactory


class ProfilePageTest(TestCase):

    def setUp(self):
        super(ProfilePageTest, self).setUp()
        self.user = UserFactory()

    def test_profile_page(self):
        url = reverse('profiles:detail')
        self.client.login(username=self.user.username, password='qwerty')
        resp = self.client.get(url)
        self.assertContains(resp, self.user.username)
