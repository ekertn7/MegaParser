from typing import Iterable
import requests
from bs4 import BeautifulSoup
from SberMegaParser.core import (
    Parser
)
from SberMegaParser.exceptions import (
    UnavailableStatusCodeException, PageCanNotLoadException
)

__all__ = ['StaticParser']


class StaticParser(Parser):
    """Static parser realisation."""
    def __init__(
        self,
        user_agent: str = None,
        cookies = None,
        proxy = None
    ):
        self.__parser = requests
        self.__headers = requests.utils.default_headers()
        if user_agent is not None:
            self.__headers.update({'User-Agent': user_agent})

    def get_html(
        self,
        url: str,
        available_status_codes: int | Iterable[int] = 200,
        timeout: int = 1
    ) -> BeautifulSoup:
        """Returns BS4 object from requested web page."""
        try:
            responce = self.__parser.get(
                url,
                timeout=timeout,
                headers=self.__headers
            )
        except requests.exceptions.Timeout as tmot:
            raise PageCanNotLoadException(timeout) from tmot
        if isinstance(available_status_codes, int):
            available_status_codes = [available_status_codes]
        if responce.status_code not in available_status_codes:
            raise UnavailableStatusCodeException(
                status_code=responce.status_code
            )
        return BeautifulSoup(responce.text, 'html.parser')


    def get(self, *args, **kwargs):
        """Returns response using requests GET method."""
        return self.__parser.get(*args, **kwargs)
