from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
from os import path
import random


REPO_URL = 'https://github.com/hjwp/book-example.git'
SITES_FOLDER = '/home/harry/sites'

def deploy():
    _create_directory_structure_if_necessary(env.host)
    source_folder = path.join(SITES_FOLDER, env.host, 'source')
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_name):
    base_folder = path.join(SITES_FOLDER, site_name)
    run('mkdir -p %s' % (base_folder))
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run('mkdir -p %s/%s' % (base_folder, subfolder))

def _get_latest_source(source_folder):
    if exists(path.join(source_folder, '.git')):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))

def _update_settings(source_folder, site_name):
    settings_path = path.join(source_folder, 'superlists/settings.py')
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    append(settings_path, 'ALLOWED_HOSTS = ["%s"]' % (site_name,))
    secret_key_file = path.join(source_folder, 'superlists/secret_key.py')
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
        append(settings_path, 'from .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = path.join(source_folder, '../virtualenv')
    if not exists(path.join(virtualenv_folder, 'bin', 'pip')):
        run('virtualenv --python=python3.3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (
            virtualenv_folder, source_folder
    ))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % (
        source_folder,
    ))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py syncdb --migrate --noinput' % (source_folder,))

