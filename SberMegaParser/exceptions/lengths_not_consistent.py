"""TBD...."""

__all__ = ['LengthsNotConsistentException']


class LengthsNotConsistentException(Exception):
    """TBD..."""
    def __init__(self):
        self.message = \
            ('Sizes of provided arguments not consists with each other '
             'and/or with objects number.'
             'Please check lengths of all arguments and objects number.')

    def __str__(self):
        return self.message
