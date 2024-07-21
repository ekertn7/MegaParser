"""Exception class when used unsupported file extension."""
from typing import Iterable

__all__ = ['UnsupporetdFileExtensionException']


class UnsupporetdFileExtensionException(Exception):
    """Exception class when used unsupported file extension."""
    def __init__(self, supported_file_extensions: Iterable[str]):
        self.message = \
            f'Unsupporetd file extension! Please, use file extension from ' \
            f'this list: {", ".join(supported_file_extensions)}!'

    def __str__(self):
        return self.message
