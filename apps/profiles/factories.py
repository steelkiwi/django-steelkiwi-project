import factory

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.webdesign import lorem_ipsum


class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    @factory.lazy_attribute
    def password(self):
        return make_password('qwerty')

    @factory.sequence
    def username(n):
        return '{0}_{1}'.format(lorem_ipsum.words(1, False), n)

    @factory.lazy_attribute_sequence
    def email(self, n):
        return '{}@example.com'.format(self.username, n)

    @factory.lazy_attribute
    def first_name(self):
        return lorem_ipsum.words(1, False).capitalize()

    @factory.lazy_attribute
    def last_name(self):
        return lorem_ipsum.words(1, False).capitalize()


class AdminFactory(UserFactory):
    username = 'admin'
    email = 'admin@example.com'
    password = make_password('admin')
    is_staff = True
    is_active = True
    is_superuser = True
