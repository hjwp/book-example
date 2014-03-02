from fabric.api import run
from fabric.context_managers import settings, shell_env


def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py'


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'elspeth@{host}'):
        run(f'{manage_dot_py} flush --noinput')

