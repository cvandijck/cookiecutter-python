import argparse
import logging
from pathlib import Path

from {{cookiecutter.package_name}} import __version__
from {{cookiecutter.package_name}}.resources import get_resource_path
from {{cookiecutter.package_name}}.exceptions import CodedError, UnknownError


LOGGER = logging.getLogger(name='{{cookiecutter.package_name}}')


def process(input_file: Path, output_file: Path, log_file: Path):
    """Function to call the application's functionality.

    Args:
        input_file: path to input file
        output_file: path to write output
        log_file: path to store log file

    Raises:
        UnknownError: raised when an unspecified exception was thrown by our application

    """
    LOGGER.info(f'Running {{cookiecutter.package_name}} {__version__}')

    try:
        # ADD YOUR CODE HERE
        ...
    except Exception as e:
        LOGGER.error(f'Unknown exception raised\n{str(e)}')
        raise UnknownError from e
    # ADD SPECIFIC EXCEPTIONS WITH ASSIGNED EXIT CODES

    LOGGER.info('Exiting successfully')


def main():
    parser = argparse.ArgumentParser(
        prog=f'{{cookiecutter.package_name}} {__version__}',
        description='{{cookiecutter.short_description}}',
    )
    parser.add_argument('input_file', help='Input file to run {{cookiecutter.package_name}}')
    parser.add_argument('output_file', help='Output of {{cookiecutter.package_name}} will be written here')

    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    try:
        process(input_file, output_file)
    except CodedError as e:
        LOGGER.error(e)
        exit(e.exit_code)
    # HANDLE SPECIFIC EXCEPTIONS AND EXIT WITH THEIR EXIT CODES


if __name__ == '__main__':
    main()
