import os

GITHUB_JOB = "GITHUB_JOB"
FORCE_NO_VENV = "FORCE_NO_VENV"

# scripts ensures a virtual environment is located in .venv and is active

WINDOWS_CREATE_VENV_CMD = "python -m venv .venv"
WINDOWS_ACTIVATE_VENV_CMD = ".venv\\Scripts\\activate.bat"

UNIX_CREATE_VENV_CMD = "python -m venv .venv"
UNIX_ACTIVATE_VENV_CMD = "source .venv/bin/activate"

if __name__ == '__main__':

    is_inside_docker = os.path.exists('/.dockerenv')
    is_inside_gh_wf = GITHUB_JOB in os.environ
    is_force_no_venv = FORCE_NO_VENV in os.environ and os.environ[FORCE_NO_VENV] == "1"

    if is_inside_docker or is_inside_gh_wf or is_force_no_venv:
        exit(0)

    if not os.path.exists(f"{os.getcwd()}/.venv"):
        print(".venv directory not found")
        msg_cmd=WINDOWS_CREATE_VENV_CMD if os.name == 'nt' else UNIX_CREATE_VENV_CMD
        print(f"run cmd '{msg_cmd}'")
        exit(1)

    if 'VIRTUAL_ENV' not in os.environ:
        print("virtual env is not active")
        msg_cmd=WINDOWS_ACTIVATE_VENV_CMD if os.name == 'nt' else UNIX_ACTIVATE_VENV_CMD
        print(f"run cmd '{msg_cmd}'")
        exit(1)

    exit(0)
