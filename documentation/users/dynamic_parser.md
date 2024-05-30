[назад](/README.md)

# Документация для модуля Dynamic Parser

Класс DynamicParser создает объект WebDriver с заданными параметрами.

Параметры:
- __dynamic_parser_type__: выбор браузера и вебдравера для запуска (задается с помощью предопределенного класса _DynamicParserType_, в котором перечислены допустимые параметры браузеров)
- __headless__: запуск браузера в скрытом режиме (не рекомендуется для отладки)
- __window_width__: ширина окна браузера
- __window_height__: высота окна браузера

Пример инициализации парсера динамических веб-сайтов:
```python
from SberMegaParser import DynamicParser, DynamicParserType

parser_1 = DynamicParser(
    DynamicParserType.firefox, # выбираем firefox в качестве браузера
    window_width=300,
    window_height=700,
    headless=False
)
```

Для запуска динамического парсера необходимо использовать метод _open_connection_.
```python
parser_1.open_connection()
```

Для остановки динамического парсера необходимо использовать метод _close_connection_.
```python
parser_1.close_connection()
```
