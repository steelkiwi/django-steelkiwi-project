import sys

from split_settings.tools import optional, include
from unipath import Path

PROJECT_PATH = Path()


def rel(*x):
    return PROJECT_PATH.child(*x).absolute()

sys.path.insert(1, str(rel('apps')))

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
    scope=locals()
)
