from django.contrib import admin

from authtools.admin import NamedUserAdmin

from .models import User

admin.site.register(User, NamedUserAdmin)
