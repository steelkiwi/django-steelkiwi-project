# -*- coding: utf-8 -*-
from .base import rel

STATIC_ROOT = rel('public', 'static')
MEDIA_ROOT = rel('public', 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
