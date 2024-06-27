"""Exception class when received unavailable status code in HTTP response."""
from collections import namedtuple

__all__ = ['UnavailableStatusCodeException']


StatusCode = namedtuple('StatusCode', ('category', 'explanation'))


status_code_explanations = {
    100: StatusCode('Informational', 'Continue'),
    101: StatusCode('Informational', 'Switching protocols'),
    102: StatusCode('Informational', 'Processing'),
    103: StatusCode('Informational', 'Early hints'),
    200: StatusCode('Success',       'Successful response'),
    201: StatusCode('Success',       'Created'),
    202: StatusCode('Success',       'Accepted'),
    203: StatusCode('Success',       'Non-authoritative information'),
    204: StatusCode('Success',       'No content'),
    205: StatusCode('Success',       'Reset content'),
    206: StatusCode('Success',       'Partial content'),
    207: StatusCode('Success',       'Multi-status'),
    208: StatusCode('Success',       'Already reported'),
    226: StatusCode('Success',       'I\'m used'),
    300: StatusCode('Redirection',   'Multiple choices'),
    301: StatusCode('Redirection',   'Moved permanently'),
    302: StatusCode('Redirection',   'Found'),
    303: StatusCode('Redirection',   'See other'),
    304: StatusCode('Redirection',   'Not modified'),
    305: StatusCode('Redirection',   'Use proxy'),
    306: StatusCode('Redirection',   'You found a dinosaur'),
    307: StatusCode('Redirection',   'Temporary redirect'),
    308: StatusCode('Redirection',   'Permanent redirect'),
    400: StatusCode('Client error',  'Bad request'),
    401: StatusCode('Client error',  'Unauthorized'),
    402: StatusCode('Client error',  'Payment required'),
    403: StatusCode('Client error',  'Forbidden'),
    404: StatusCode('Client error',  'Page not found'),
    405: StatusCode('Client error',  'Method not allowed'),
    406: StatusCode('Client error',  'Not acceptable'),
    407: StatusCode('Client error',  'Proxy authentication required'),
    408: StatusCode('Client error',  'Requests timeout'),
    409: StatusCode('Client error',  'Conflict'),
    410: StatusCode('Client error',  'Gone'),
    411: StatusCode('Client error',  'Length required'),
    412: StatusCode('Client error',  'Precondition failed'),
    413: StatusCode('Client error',  'Payload too large'),
    414: StatusCode('Client error',  'URI too long'),
    415: StatusCode('Client error',  'Unsupported media type'),
    416: StatusCode('Client error',  'Range not satisfiable'),
    417: StatusCode('Client error',  'Expectation failed'),
    418: StatusCode('Client error',  'I\'am a teapot'),
    419: StatusCode('Client error',  'Authentication timeout'),
    421: StatusCode('Client error',  'Misdirected requests'),
    422: StatusCode('Client error',  'Unprocessable entity'),
    423: StatusCode('Client error',  'Locked'),
    424: StatusCode('Client error',  'Failed dependency'),
    425: StatusCode('Client error',  'Too early'),
    426: StatusCode('Client error',  'Upgrade required'),
    428: StatusCode('Client error',  'Precondition required'),
    429: StatusCode('Client error',  'Too many requests'),
    431: StatusCode('Client error',  'Request header fields too large'),
    449: StatusCode('Client error',  'Retry with'),
    451: StatusCode('Client error',  'Unavailable for legal reasons'),
    499: StatusCode('Client error',  'Client closed requests'),
    500: StatusCode('Server error',  'Internal server error'),
    501: StatusCode('Server error',  'Not implemented'),
    502: StatusCode('Server error',  'Bad gateway'),
    503: StatusCode('Server error',  'Service unavailable'),
    504: StatusCode('Server error',  'Gateway timeout'),
    505: StatusCode('Server error',  'HTTP version not supported'),
    506: StatusCode('Server error',  'Variant also negotiates'),
    507: StatusCode('Server error',  'Insufficient storage'),
    508: StatusCode('Server error',  'Loop detected'),
    509: StatusCode('Server error',  'Bandwidth limit exceeded'),
    510: StatusCode('Server error',  'Not extended'),
    511: StatusCode('Server error',  'Network authentication required'),
    520: StatusCode('Server error',  'Unknown error'),
    521: StatusCode('Server error',  'Web server is down'),
    522: StatusCode('Server error',  'Connection timed out'),
    523: StatusCode('Server error',  'Origin is unreachable'),
    524: StatusCode('Server error',  'A timeout occurred'),
    525: StatusCode('Server error',  'SSL handshake failed'),
    526: StatusCode('Server error',  'Invalid SSL certificate'),
}


class UnavailableStatusCodeException(Exception):
    """Exception class when received unavailable status code in HTTP response."""
    def __init__(self, status_code: int):
        try:
            self.message = \
                f'Unavailable status code to continue: {status_code} (' \
                f'{status_code_explanations[status_code].category}, ' \
                f'{status_code_explanations[status_code].explanation})! ' \
                f'Try to fix this error and connect to the server again!'
        except KeyError:
            self.message = \
                f'Unavailable status code to continue: {status_code}! ' \
                f'Try to fix this error and connect to the server again!'

    def __str__(self):
        return self.message
