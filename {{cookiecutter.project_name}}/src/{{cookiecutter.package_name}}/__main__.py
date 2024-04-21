import argparse
import logging
import sys

import {{cookiecutter.package_name}}
from {{cookiecutter.package_name}} import __version__
from {{cookiecutter.package_name}}.resources import get_resource_path, PathType
from {{cookiecutter.package_name}}.exceptions import UnknownError


def parse_console_arguments():
    """ Parses commandline arguments provided to the console script """

    # Using argparse as a default main function. Change arguments or remove all together.
    parser = argparse.ArgumentParser(prog='{{cookiecutter.package_name}} {}'.format(__version__),
                                     description='{{cookiecutter.short_description}}')
    parser.add_argument('input_file', help='Input file to run {{cookiecutter.package_name}}')
    parser.add_argument('output_file', help='Output of {{cookiecutter.package_name}} will be written here')
    parser.add_argument('--log_file', '-l', help='Optional custom log file name', default='logging.log')
    parser.add_argument('--status_file', '-s', help='Optional custom status file name', default='status.json')

    args = parser.parse_args()
    input_file = vars(args)['input_file']
    output_file = vars(args)['output_file']
    log_file = vars(args)['log_file']
    status_file = vars(args)['status_file']

    return input_file, output_file, log_file, status_file


def process(input_file: PathType, output_file: PathType, log_file: PathType, status_file: PathType):
    """ Function to call the application's functionality

    Args:
        input_file: path to input file
        output_file: path to write output
        log_file: path to store log file
        status_file: path to store status file

    Raises:
        UnknownError: raised when an unspecified exception was thrown by our application

    """
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')
    logging.log(logging.INFO, 'Running {{cookiecutter.package_name}} {}'.format(__version__))

    try:
        # ADD YOUR CODE HERE
        ...
    except Exception as e:
        logging.log(logging.ERROR, 'Unknown exception raised\n{}'.format(str(e)))
        raise UnknownError from e
    # ADD SPECIFIC EXCEPTIONS WITH ASSIGNED EXIT CODES

    logging.log(logging.INFO, 'Exiting successfully')


def main():
    input_file, output_file, log_file, status_file = parse_console_arguments()
    try:
        process(input_file, output_file, log_file, status_file)
    except UnknownError as e:
        print(e, file=sys.stderr)
        exit(e.exit_code)
    # HANDLE SPECIFIC EXCEPTIONS AND EXIT WITH THEIR EXIT CODES


if __name__ == '__main__':
    main()
