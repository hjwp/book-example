from fabric.api import env, run


def _get_paths(host):
    base_folder = '~/sites/{host}'.format(host=host)
    manage_py = '{path}/virtualenv/bin/python {path}/source/manage.py'.format(
        path=base_folder
    )
    return base_folder, manage_py


def reset_database():
    base_folder, manage_py = _get_paths(env.host)
    run('rm -f {path}/database/database.sqlite'.format(path=base_folder))
    run('{manage_py} syncdb --noinput'.format(manage_py=manage_py))
    run('{manage_py} migrate'.format(manage_py=manage_py))


def create_session_on_server():
    base_folder, manage_py = _get_paths(env.host)
    session_key = run('{manage_py} create_session'.format(manage_py=manage_py))
    print(session_key)

