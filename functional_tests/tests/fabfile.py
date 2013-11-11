from fabric.api import env, run


def _get_base_folder(host):
    return '~/sites/{host}'.format(host=host)

def _get_manage_dot_py(host):
    return '{path}/virtualenv/bin/python {path}/source/manage.py'.format(
        path=_get_base_folder(host)
    )


def reset_database():
    run('rm -f {path}/database/database.sqlite'.format(
        path=_get_base_folder(env.host)
    ))
    run('{manage_py} syncdb --migrate --noinput'.format(
        manage_py=_get_manage_dot_py(env.host)
    ))


def create_session_on_server():
    session_key = run('{manage_py} create_session'.format(
        manage_py=_get_manage_dot_py(env.host)
    ))
    print(session_key)

