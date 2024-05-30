# Универсальный парсер

# Инструкция для пользователей

Для начала необходимо определиться с тем, какой сайт вы собираетесь парсить
- __статический/простой__ веб-сайт (весь контент виден сразу после загрузки страницы) ([пример](https://ru.wikipedia.org/wiki/Веб-скрейпинг))
- __динамический/сложный__ веб-сайт (при наведении/клике на элементы или скролле страницы появляется дополнительный контент, который нельзя получить с помощью генерации адреса) ([пример](https://megamarket.ru))
    - необходимо скачать браузер из списка поддерживаемых браузеров
        - google chrome
        - mozilla firefox
    - необходимо скачать вебдрайвер и разместить его в корне проекта
        - [вебдрайвер](https://sites.google.com/chromium.org/driver/downloads) для google chrome
        - [вебдрайвер](https://github.com/mozilla/geckodriver/releases) для mozilla firefox
    - пример работы динамического парсера представлен в демонстрационном ноутбуке [demo/dynamic_parser.ipynb](./demo/dynamic_parser.ipynb)
    - [инструкция](/documentation/users/dynamic_parser.md) по работе с динамическим парсером

# Инструкция для разработчиков

В данном проекте мы __работаем по TDD__ (сначала пишем тесты, потом уже на основе тестов пишем код).
Версия __Python 3.12__.

С дорожной картой можно ознакомиться [здесь](/documentation/developers/road_map.md).

Установите [editorconfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) для VSCode. PyCharm поддерживает editorconfig из коробки.

Настройте pytest:
- __для VSCode__: кликаем на микстурку в левом меню (testing) -> configure python tests -> pytest -> _. root directory_ -> обновляем менюшку
- __для PyCharm__: кликаем settings -> вбиваем в поиск "runner" -> testing -> default test runner -> выбрать _pytest_ из выпадающего меню

[Соглашение по коду](/documentation/developers/code_rules.md) для тех, кто подключился к проекту впервые.
