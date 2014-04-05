# -*- coding: utf-8 -*-
from unipath import Path

PROJECT_PATH = Path()

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DOMAIN = '{{ project_name }}.pirsipy.com'
ALLOWED_HOSTS = [DOMAIN]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECRET_KEY = '{{ secret_key }}'
ROOT_URLCONF = 'common.urls'
WSGI_APPLICATION = 'wsgi.application'


def rel(*x):
    return PROJECT_PATH.child(*x)
