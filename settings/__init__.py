from split_settings.tools import optional, include

SITE_ID = 1
PROJECT_NAME = '{{ project_name }}'


def export(space=None):
    if space is None:
        space = locals()
        space['__file__'] = __file__
        space['SITE_ID'] = SITE_ID
        space['PROJECT_NAME'] = PROJECT_NAME

    include(
        'components/base.py',
        'components/auth.py',
        'components/locale.py',
        'components/static.py',
        'components/templates.py',
        'components/db_and_cache.py',
        'components/middleware.py',
        'components/apps.py',
        'components/logging.py',
        optional('local.py'),

        scope=space
    )
    return space

export(locals())
