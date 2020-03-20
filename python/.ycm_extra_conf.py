import os
from subprocess import Popen, PIPE


def Settings(**kwargs):
    cmd = Popen(
        "pipenv --venv", shell=True, stdout=PIPE, stderr=PIPE
    )

    stdout, _ = cmd.communicate()

    interpreter_path = stdout.decode("utf-8").strip()

    if cmd.returncode or not os.path.isdir(interpreter_path):
        return {}

    return {
        "interpreter_path": "{0:s}/bin/python".format(interpreter_path)
    }
