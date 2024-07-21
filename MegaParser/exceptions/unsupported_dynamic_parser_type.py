"""Exception class when used unsupported DynamicParserType."""
from MegaParser.core.dynamic_parser.dynamic_parser_type import (
    DynamicParserType
)

__all__ = ['UnsupporetdDynamicParserTypeException']


class UnsupporetdDynamicParserTypeException(Exception):
    """Exception class when used unsupported DynamicParserType."""
    def __init__(self):
        self.message = \
            f'Unsupporetd DynamicParserType! Please, select dynamic parser ' \
            f'type using {type(DynamicParserType)}!'

    def __str__(self):
        return self.message
