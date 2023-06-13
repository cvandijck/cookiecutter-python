import subprocess
import sys
from pathlib import Path


def main(args):
    package_folder = Path(__file__).resolve().parents[1]
    dist_folder = package_folder / 'dist'
    dep_folder = package_folder / 'dependencies'
    wheel_files = list(dist_folder.glob('{{cookiecutter.package_name}}-*.whl'))

    if len(wheel_files) == 0:
        return 'No valid package wheel found'

    latest_wheel_file = wheel_files[-1]

    print('Install latest wheel', latest_wheel_file)
    process = subprocess.run([sys.executable, '-m', 'pip', 'install', latest_wheel_file, '--find-links', dep_folder],
                             cwd=package_folder, universal_newlines=True, shell=True)

    return process.returncode


if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
