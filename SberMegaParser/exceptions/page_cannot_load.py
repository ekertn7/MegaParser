"""Exception class when requested page can not be load."""

__all__ = ['PageCanNotLoadException']


class PageCanNotLoadException(Exception):
    """Exception class when requested page can not be load."""
    def __init__(self, timeout: int = None):
        if timeout:
            self.message = f'Requested page can not be load in {timeout} ' \
                           f'seconds!'
        else:
            self.message = 'Requested page can not be load!'

    def __str__(self):
        return self.message
