from typing import List
from MegaParser.core.dynamic_parser import dynamic_parser
from MegaParser.core.dynamic_parser import dynamic_parser_type
from MegaParser.core.factories import parser_factory
from MegaParser.exceptions import LengthsNotConsistentException
from MegaParser.tools.proxy.dynamic_parser_proxy import DynamicParserProxy

__all__ = ['DynamicParserFactory']


class DynamicParserFactory(parser_factory.ParserFactory):
    def __init__(self,
                 objects_number: int = 1,
                 cookies: List = None,
                 user_agents: List[str] = None,
                 proxies: List[DynamicParserProxy] = None,
                 **kwargs):
        self.objects_number = objects_number

        self.cookies = cookies if cookies is not None \
            else parser_factory.create_nulls_collection(objects_number)

        self.user_agents = user_agents if user_agents is not None \
            else parser_factory.create_nulls_collection(objects_number)

        self.proxies = proxies if proxies is not None \
            else parser_factory.create_nulls_collection(objects_number)

        if not (len(self.cookies) == len(self.user_agents) ==
                len(self.proxies) == self.objects_number):
            raise LengthsNotConsistentException()

        self.window_width = kwargs.get('window_width', 700)
        self.window_height = kwargs.get('window_height', 400)
        self.headless = kwargs.get('headless', False)

    def get_parsers(self):
        for i in range(self.objects_number):
            parser = dynamic_parser.DynamicParser(
                dynamic_parser_type.DynamicParserType.firefox,
                window_width=self.window_width,
                window_height=self.window_height,
                headless=self.headless,
                cookies=self.cookies[i],
                user_agent=self.user_agents[i],
                proxy=self.proxies[i]
            )

            yield parser
