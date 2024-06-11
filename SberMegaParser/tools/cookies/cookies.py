__all__ = ['import_cookies']
import json
import traceback
import requests

def import_cookies():
    pass

class CookiesWorker():
    def save_cookies(self,parser_object, cookies_filename='cookie_file'):
        parser_type = str(type(parser_object))
        try:
            if 'selenium' in parser_type:
                cookies = parser_object.get_cookies()
            elif 'requests' in parser_type:
                cookies = requests.utils.dict_from_cookiejar(parser_object.cookies)
            else:
                raise TypeError(f'Неподдерживаемый тип парсера')
            with open(cookies_filename, 'w') as cookies_file:
                json.dump(cookies, cookies_file)
        except:
            print(traceback.format_exc())

    def load_cookies(self,cookies_path):
        try:
            with open(cookies_path, 'r') as cookies_file:
                cookies = json.load(cookies_file)
            return cookies
        except:
            print(traceback.format_exc())
