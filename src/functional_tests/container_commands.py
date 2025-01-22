import subprocess

USER = "elspeth"


def reset_database(host):
    return _exec_in_container(
        host, ["/venv/bin/python", "/src/manage.py", "flush", "--noinput"]
    )


def create_session_on_server(host, email):
    return _exec_in_container(
        host, ["/venv/bin/python", "/src/manage.py", "create_session", email]
    )


def _exec_in_container(host, commands):
    if "localhost" in host:
        return _exec_in_container_locally(commands)
    else:
        return _exec_in_container_on_server(host, commands)


def _exec_in_container_locally(commands):
    print(f"Running {commands} on inside local docker container")
    return _run_commands(["docker", "exec", _get_container_id()] + commands)


def _exec_in_container_on_server(host, commands):
    print(f"Running {commands!r} on {host} inside docker container")
    return _run_commands(
        ["ssh", f"{USER}@{host}", "docker", "exec", "superlists"] + commands
    )


def _get_container_id():
    return subprocess.check_output(
        ["docker", "ps", "-q", "--filter", "ancestor=superlists"]
    ).strip()


def _run_commands(commands):
    process = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    result = process.stdout.decode()
    if process.returncode != 0:
        raise Exception(result)
    print(f"Result: {result!r}")
    return result.strip()
