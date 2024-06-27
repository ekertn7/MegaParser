from typing import Iterable
import requests
from bs4 import BeautifulSoup
from SberMegaParser.core import (
    Parser
)
from SberMegaParser.exceptions import (
    UnavailableStatusCodeException
)

__all__ = ['StaticParser']


class StaticParser(Parser):
    def __init__(
        self,
        user_agent = None,
        cookies = None,
        proxy = None
    ):
        self.__parser = requests

    def get_html(
        self,
        url: str,
        available_status_codes: int | Iterable[int] = 200
    ) -> BeautifulSoup:
        responce = self.__parser.get(url)
        if isinstance(available_status_codes, int):
            available_status_codes = [available_status_codes]
        if responce.status_code in available_status_codes:
            return BeautifulSoup(responce.text, 'html.parser')
        else:
            raise UnavailableStatusCodeException(
                status_code=responce.status_code
            )

    def get(self, *args, **kwargs):
        return self.__parser.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.__parser.post(*args, **kwargs)
