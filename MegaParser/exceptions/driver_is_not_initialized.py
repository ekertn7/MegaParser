"""Exception class when trying to access a non-existent webdriver object."""

__all__ = ['DriverIsNotInitializedException']


class DriverIsNotInitializedException(Exception):
    """Exception class when trying to access a non-existent webdriver object."""
    def __init__(self):
        self.message = \
            'Web driver object is not initialized! Please, create web driver ' \
            'object using open_connection method before use other methods!'

    def __str__(self):
        return self.message
