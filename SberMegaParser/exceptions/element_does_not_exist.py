"""Exception class when requested element does not exist."""

__all__ = ['ElementDoesNotExistException']


class ElementDoesNotExistException(Exception):
    """Exception class when requested element does not exist."""
    def __init__(self):
        self.message = 'Requested element does not exist!'

    def __str__(self):
        return self.message
