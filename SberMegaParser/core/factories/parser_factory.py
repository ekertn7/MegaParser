from abc import ABC, abstractmethod


class ParserFactory(ABC):

    @abstractmethod
    def create(self):
        pass

    def _create_nulls_collection(self, length):
        return [None for _ in range(length)]
