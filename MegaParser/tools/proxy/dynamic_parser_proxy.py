from dataclasses import dataclass

__all__ = ['DynamicParserProxy']


@dataclass
class DynamicParserProxy:
    host: str
    port: str
    username: str
    password: str
