import subprocess
import sys
from pathlib import Path


def main(args):
    package_folder = Path(__file__).resolve().parents[1]
    dist_folder = package_folder / 'dist'
    dep_folder = package_folder / 'dependencies'

    try:
        print('Clean build folder to avoid taking elements from previous builds')
        subprocess.run([sys.executable, 'setup.py', 'clean', '--all'], cwd=package_folder,
                       universal_newlines=True, check=True, shell=True)

        print('Building wheel file to dist folder')
        subprocess.run([sys.executable, '-m', 'pip', 'wheel', package_folder, '--no-deps', '--find-links', dep_folder,
                        '-w', dist_folder], cwd=package_folder, universal_newlines=True, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        return e.returncode


if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
