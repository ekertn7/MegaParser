"""Exception class when trying to create an already initialized webdriver
object."""

__all__ = ['DriverAlreadyInitializedException']


class DriverAlreadyInitializedException(Exception):
    """Exception class when trying to create an already initialized webdriver
    object."""
    def __init__(self):
        self.message = \
            'Web driver object is already initialized! Please, close old ' \
            'connection using close_connection method and try again!'

    def __str__(self):
        return self.message
