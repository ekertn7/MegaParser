"""Exception class when used unsupported DynamicParserType."""

__all__ = ['UnsupporetdDynamicParserTypeException']


class UnsupporetdDynamicParserTypeException(Exception):
    """Exception class when used unsupported DynamicParserType."""
    def __init__(self):
        self.message = \
            f'Unsupporetd DynamicParserType! Please, choice dynamic parser ' \
            f'type from SberMegaParser.core.dynamic_parser.DynamicParserType ' \
            f'class!'

    def __str__(self):
        return self.message
