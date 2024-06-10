from SberMegaParser.core import DynamicParser, DynamicParserType
from SberMegaParser.core.factories import ParserFactory


class DynamicParserFactory(ParserFactory):
    def __init__(self):
        pass

    # пока так, в идеале пробросить параметры в create
    def create(self):
        parser = DynamicParser(
            DynamicParserType.firefox,
            window_width=300,
            window_height=700,
            headless=False
        )

        return parser
