from collections.abc import Iterable
from SberMegaParser.core.dynamic_parser import DynamicParser, DynamicParserType
from SberMegaParser.core.factories import ParserFactory, create_nulls_collection

__all__ = ['DynamicParserFactory']


class DynamicParserFactory(ParserFactory):
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

        self.window_width = kwargs.get('window_width', 700)
        self.window_height = kwargs.get('window_height', 400)
        self.headless = kwargs.get('headless', False)

    def get_parsers(self):
        for i in range(self.objects_number):
            parser = DynamicParser(
                DynamicParserType.firefox,
                window_width=self.window_width,
                window_height=self.window_height,
                headless=self.headless,
                cookies=self.cookies[i],
                user_agent=self.user_agents[i],
                proxy=self.proxies[i]
            )

            yield parser
