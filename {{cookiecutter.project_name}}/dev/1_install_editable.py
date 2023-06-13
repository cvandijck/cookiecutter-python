import subprocess
import sys
from pathlib import Path


def main(args):
    package_folder = Path(__file__).resolve().parents[1]
    dep_folder = package_folder / 'dependencies'

    print('Install {{cookiecutter.package_name}} as editable package')
    process = subprocess.run([sys.executable, '-m', 'pip', 'install', '-e', '.[dev]', '--find-links', dep_folder,
                              '--upgrade'], cwd=package_folder, universal_newlines=True, shell=True)
    return process.returncode


if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
