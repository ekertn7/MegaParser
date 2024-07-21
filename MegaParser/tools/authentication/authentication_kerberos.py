import requests
from requests_kerberos import HTTPKerberosAuth, DISABLED

__all__ = ['authentication_kerberos']


def authentication_kerberos(url: str) -> None:
    """
    Authentication with Kerperos.
    Can be used with DynamicParser and StaticParser.

    Args:
        url : Website url.
    """
    requests.packages.urllib3.disable_warnings(
        category=requests.packages.urllib3.exceptions.InsecureRequestWarning
    )
    kerberos_auth = HTTPKerberosAuth(
        mutual_authentication=DISABLED
    )
    requests.get(
        url,
        verify=False,
        auth=kerberos_auth
    )
