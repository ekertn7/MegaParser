import json
from SberMegaParser.core.parser import Parser

__all__ = ['extract_and_save_cookies', 'load_cookies_from_file']


DEFAULT_COOKIES_FILE_PATH = '. cookie'


def extract_and_save_cookies(
    parser: Parser,
    file_path: str = DEFAULT_COOKIES_FILE_PATH
):
    extracted_cookies = parser.get_cookies()
    _save_cookies(extracted_cookies, file_path)


def load_cookies_from_file(
    file_path: str = DEFAULT_COOKIES_FILE_PATH
):
    return _read_cookies(file_path)


def _save_cookies(cookies, file_path: str = DEFAULT_COOKIES_FILE_PATH):
    with open(file_path, 'w', encoding='utf-8') as cookies_file:
        json.dump(cookies, cookies_file)


def _read_cookies(file_path: str = DEFAULT_COOKIES_FILE_PATH):
    with open(file_path, 'r', encoding='utf-8') as cookies_file:
        cookies = json.load(cookies_file)
    return cookies
