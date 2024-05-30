from abc import ABC, abstractmethod

__all__ = ['Parser']


class Parser(ABC):
    """
    Base class to implement all parsers realisations (for dynamic and static
    websites).
    """
