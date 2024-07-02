from SberMegaParser import StaticParser
from SberMegaParser import ParserFactory

__all__ = ['StaticParserFactory']


class StaticParserFactory(ParserFactory):
    def __init__(self):
        pass

    # TODO: после реализации статического парсера прописать точное создание
    def create(self):
        parser = StaticParser()

        return parser
