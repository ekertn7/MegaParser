import pytest
from contextlib import nullcontext as does_not_raise
from MegaParser import import_cookies


class TestImportCookies:
    def test_import_cookies_exceptions(self):
        assert import_cookies() == None
