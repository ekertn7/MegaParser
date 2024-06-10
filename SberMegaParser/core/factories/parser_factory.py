from abc import ABC, abstractmethod


class ParserFactory(ABC):

    @abstractmethod
    def create(self):
        pass
