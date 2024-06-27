"""Exception class when used unsupported DynamicParserType."""

__all__ = ['UnsupporetdDynamicParserTypeException']


class UnsupporetdDynamicParserTypeException(Exception):
    """Exception class when used unsupported DynamicParserType."""
    def __init__(self):
        self.message = \
            'Unsupporetd DynamicParserType! Please, choice dynamic parser ' \
            'type from SberMegaParser.core.dynamic_parser.DynamicParserType ' \
            'class!'

    def __str__(self):
        return self.message
