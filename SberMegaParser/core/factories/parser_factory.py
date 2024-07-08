from abc import ABC, abstractmethod

__all__ = ['ParserFactory',
           'create_nulls_collection']


def create_nulls_collection(length: int):
    return [None for _ in range(length)]


class ParserFactory(ABC):

    @abstractmethod
    def get_parsers(self):
        pass
