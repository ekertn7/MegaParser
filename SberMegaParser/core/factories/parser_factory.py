from abc import ABC, abstractmethod

__all__ = ['ParserFactory']


class ParserFactory(ABC):

    @abstractmethod
    def create(self):
        pass

    def _create_nulls_collection(self, length):
        return [None for _ in range(length)]
