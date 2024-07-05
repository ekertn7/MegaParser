__all__ = ['authentication_http']

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import traceback


def authentication_http(url:str, user:str, password:str, method='basic')->str:
    """Авторизация по HTTP/HTTPS для requests и возможно selenium."""
    try:
        if method=='basic':
            auth_method = HTTPBasicAuth(user,password)
        elif method=='digest':
            auth_method = HTTPDigestAuth(user,password)
        response = requests.get(url, auth=auth_method)
        return response
    except:
        print(f'Произошла ошибка - {traceback.format_exc()}')