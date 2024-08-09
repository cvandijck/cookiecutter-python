import logging
import subprocess
import sys

LOGGER = logging.getLogger(__name__)

INITIALIZE_REPO = {{cookiecutter.initialize_repo}}
DEFAULT_BRANCH_NAME = 'main'
REPO_URL = '{{cookiecutter.url}}.git'


def _execute_command(command: list[str]):
    LOGGER.debug(' '.join(command))
    subprocess.run(command, capture_output=True, check=True)


def is_git_installed() -> bool:
    try:
        _execute_command(['git', '--version'])
        return True
    except Exception:
        return False


def initialize_repo(repo_url: str, branch: str):
    _execute_command(['git', 'init'])
    _execute_command(['git', 'add', '.'])
    _execute_command(['git', 'commit', '-m', 'cookiecutter structure'])
    _execute_command(['git', 'branch', '-M', branch])
    _execute_command(['git', 'remote', 'add', 'origin', repo_url])
    _execute_command(['git', 'push', '-u', 'origin', branch])


if __name__ == '__main__':
    if INITIALIZE_REPO and not is_git_installed():
        LOGGER.error('git is not installed')
        sys.exit(1)

    if INITIALIZE_REPO:
        initialize_repo(repo_url=REPO_URL, branch=DEFAULT_BRANCH_NAME)
