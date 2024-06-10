from SberMegaParser.core import StaticParser
from SberMegaParser.core.factories import ParserFactory


class StaticParserFactory(ParserFactory):
    def __init__(self):
        pass

    # TODO: после реализации статического парсера прописать точное создание
    def create(self):
        parser = StaticParser()

        return parser
