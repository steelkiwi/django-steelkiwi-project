PROJECT_NAME = '{{ project_name }}'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DOMAIN = os.environ['DOMAIN']
ALLOWED_HOSTS = [DOMAIN]

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']

SECRET_KEY = os.environ['SECRET_KEY']
ROOT_URLCONF = 'common.urls'
WSGI_APPLICATION = 'wsgi.application'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
