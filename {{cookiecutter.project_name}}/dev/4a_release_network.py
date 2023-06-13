import re
import shutil
import subprocess
import sys
from pathlib import Path

from {{cookiecutter.package_name}} import __version__

# Set REMOTE_DEPLOYMENT_DIR to the main folder to deploy the different versions of {{cookiecutter.project_name}}
REMOTE_DEPLOYMENT_DIR = None


def main(args):
    package_folder = Path(__file__).resolve().parents[1]
    dist_folder = package_folder / 'dist'
    dep_folder = package_folder / 'dependencies'
    doc_folder = package_folder / 'docs'

    if not REMOTE_DEPLOYMENT_DIR:
        return 'REMOTE_DEPLOYMENT_DIR not set'

    if 'dirty' in __version__ or re.match(r'\+\d.g', __version__):
        return 'Version of {{cookiecutter.package_name}} ({}) does not correspond to a final version'.format(__version__)

    try:
        wheel_file = next(dist_folder.glob('{{cookiecutter.package_name}}-{}-*.whl'.format(__version__)))
    except StopIteration:
        return 'No wheel file of {{cookiecutter.package_name}} found that corresponds to current version {}'.format(__version__)

    release_dir = Path(REMOTE_DEPLOYMENT_DIR).resolve() / __version__
    release_dir.mkdir(exist_ok=True)

    print('This script will deploy the packaged wheel, documentation and dependencies to a remote location:')
    print(' ', release_dir)

    print('Copy documentation')
    p = subprocess.run(['robocopy', doc_folder / '_build' / 'html', release_dir / 'docs', '/MIR', '/NP'],
                       cwd=package_folder, universal_newlines=True, check=False, shell=True)
    if p.returncode > 7:
        return 'Copy documentation failed: {}'.format(exit_code)

    print('Copy package')
    p = subprocess.run(['robocopy', wheel_file.parent, release_dir / 'package', wheel_file.name, '/MIR', '/NP'],
                       cwd=package_folder, universal_newlines=True, check=False, shell=True)
    if p.returncode > 7:
        return 'Copy package failed: {}'.format(exit_code)

    print('Copy dependencies')
    p = subprocess.run(['robocopy', dep_folder, release_dir / 'dependencies', '/MIR', '/NP'],
                       cwd=package_folder, universal_newlines=True, check=False, shell=True)
    if p.returncode > 7:
        return 'Copy dependencies failed: {}'.format(exit_code)
    return 0


if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
