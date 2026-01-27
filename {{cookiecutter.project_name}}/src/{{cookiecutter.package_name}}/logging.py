import logging
import re
import sys
from pathlib import Path
from typing import Literal, Optional

DEFAULT_LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
PACKAGE_REGEX = re.compile(r'^{{cookiecutter.package_name}}\.')
MAIN_REGEX = re.compile(r'^__main__$')


def configure_logging(
    level: int = logging.INFO,
    log_format: str = DEFAULT_LOGGING_FORMAT,
    log_file_path: Optional[Path] = None,
    log_file_mode: Literal['w', 'a'] = 'a',
    external_log_level: int = logging.WARNING,
    only_log_to_file: bool = False,
):
    root_logger = logging.getLogger()
    root_logger.setLevel(external_log_level)  # set root logger to external log level

    formatter = logging.Formatter(log_format)

    if only_log_to_file and log_file_path is None:
        raise ValueError('log_file_path must be provided if only_log_to_file is True')

    if not only_log_to_file:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        root_logger.addHandler(console_handler)

    if log_file_path:
        file_handler = logging.FileHandler(filename=str(log_file_path), mode=log_file_mode)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        root_logger.addHandler(file_handler)

    # ensure existing loggers have correct levels
    for logger in get_all_loggers(include_root=False):
        if PACKAGE_REGEX.match(logger.name) or MAIN_REGEX.match(logger.name):
            logger.setLevel(level)
        else:
            logger.setLevel(external_log_level)


def get_all_loggers(include_root: bool = False, name_regex_filter: Optional[re.Pattern] = None) -> list[logging.Logger]:
    if not name_regex_filter:
        name_regex_filter = re.compile('.*')
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict if name_regex_filter.match(name)]
    if include_root:
        loggers = [logging.getLogger()] + loggers
    return loggers


def convert_logging_level(level: str) -> int:
    # in python 3.11 logging.getLevelName is deprecated

    if sys.version_info < (3, 11):
        return logging.getLevelName(level)

    mapping = logging.getLevelNamesMapping()

    if level.upper() not in mapping:
        raise ValueError(f'Invalid log level: {level}')

    return mapping[level.upper()]
