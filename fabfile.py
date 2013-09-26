from fabric.api import run, env, cd, prefix, task, roles

ENV_MAP = {
    'test': {'hosts': '{{ project_name }}.steelkiwi.com',
             'user': 'webmaster',
             'path': '/home/webmaster/www/{{ project_name }}.steelkiwi.com',
             'branch': 'master'}}

ENV_COMMAND = 'source env/bin/activate'

for k, v in ENV_MAP['test'].iteritems():
    setattr(env, k, v)


def set_env(deploy_type):
    if deploy_type not in ENV_MAP.keys():
        raise KeyError('Choose from list: {}'.format(ENV_MAP.keys()))
    env.type = deploy_type
    for k, v in ENV_MAP[deploy_type].iteritems():
        setattr(env, k, v)


def manage(command):
    with cd(env.path), prefix(ENV_COMMAND):
        run('python manage.py {}'.format(command))


@task
def update(deploy_type='test'):
    set_env(deploy_type)
    with cd(env.path):
        run('git pull origin {}'.format(env.branch))
        run('find . -name "*.pyc" -exec rm -f {} \;')
        requirements()
        db()
        collectstatic()
        restart()


@task
def requirements():
    with cd(env.path), prefix(ENV_COMMAND):
        run('pip install --exists-action=s -r requirements.txt')


@task
def db():
    syncdb()
    migrate()


@task
def syncdb():
    manage('syncdb  --noinput -v 0')


@task
def migrate():
    manage('migrate -v 0')


@task
def collectstatic():
    manage('collectstatic --noinput')


@task
def restart():
    run('supervisorctl restart {}:'.format(env.type))


@task
def status(deploy_type='test'):
    set_env(deploy_type)
    run('supervisorctl status')
