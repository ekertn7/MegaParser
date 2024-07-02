from collections.abc import Iterable
from SberMegaParser import DynamicParser, DynamicParserType
from SberMegaParser.core.factories import ParserFactory

__all__ = ['DynamicParserFactory']


class DynamicParserFactory(ParserFactory):
    def __init__(self,
                 objects_number: int = 1,
                 cookies: Iterable=None,
                 user_agents: Iterable[str]=None,
                 proxies: Iterable[str]=None):

        self.objects_number = objects_number

        self.cookies = cookies if cookies is not None \
            else self._create_nulls_collection(objects_number)

        self.user_agents = user_agents if user_agents is not None \
            else self._create_nulls_collection(objects_number)

        self.proxies = proxies if proxies is not None \
            else self._create_nulls_collection(objects_number)

    # пока так, в идеале пробросить параметры в create
    def create(self):
        for i in range(self.objects_number):
            parser = DynamicParser(
                DynamicParserType.firefox,
                # вот эту красоту перекидываем на kwargs
                window_width=300,
                window_height=700,
                headless=False,
                # -------
                cookies=self.cookies[i],
                user_agent=self.user_agents[i],
                proxy=self.proxies[i]
            )

            yield parser
