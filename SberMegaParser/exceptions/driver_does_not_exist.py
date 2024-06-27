"""Exception class when trying to create a webdriver object, but webdriver does
not exist in system."""
from typing import assert_never
from SberMegaParser.core.dynamic_parser.dynamic_parser_type import (
    DynamicParserType
)

__all__ = ['DriverDoesNotExistException']


class DriverDoesNotExistException(Exception):
    """Exception class when trying to create a webdriver object, but webdriver
    does not exist in system."""
    def __init__(self, parser_type):
        match type(parser_type):
            case DynamicParserType.chrome.value:
                self.message = \
                    'Install webdriver for Chrome from https://sites.google.' \
                    'com/chromium.org/driver/downloads and put this file ' \
                    'into the project\'s root directory please!'
            case DynamicParserType.firefox.value:
                self.message = \
                    'Install webdriver for FireFox from https://github.com/' \
                    'mozilla/geckodriver/releases and put this file ' \
                    'into the project\'s root directory please!'
            case _ as unreachable:
                assert_never(unreachable)

    def __str__(self):
        return self.message
