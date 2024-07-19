from collections.abc import Iterable
from SberMegaParser.core.static_parser import *
from SberMegaParser.core.factories import *

__all__ = ['StaticParserFactory']


class StaticParserFactory(ParserFactory):
    def __init__(self,
                 objects_number: int = 1,
                 cookies: Iterable = None,
                 user_agents: Iterable[str] = None,
                 proxies: Iterable[str] = None,
                 **kwargs):
        self.objects_number = objects_number

        self.cookies = cookies if cookies is not None \
            else create_nulls_collection(objects_number)

        self.user_agents = user_agents if user_agents is not None \
            else create_nulls_collection(objects_number)

        self.proxies = proxies if proxies is not None \
            else create_nulls_collection(objects_number)

    def get_parsers(self):
        for i in range(self.objects_number):
            parser = StaticParser(
                cookies=self.cookies[i],
                user_agent=self.user_agents[i],
                proxy=self.proxies[i]
            )
            yield parser