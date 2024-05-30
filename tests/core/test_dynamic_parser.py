import pytest
from enum import Enum
from contextlib import nullcontext as does_not_raise
from SberMegaParser import DynamicParser, DynamicParserType
from SberMegaParser import UnsupporetdDynamicParserTypeException


class FakeDynamicParserTypeChrome:
    def __init__(self, headless, window_width, window_height):
        self.options = []


class FakeDynamicParserTypeFirefox:
    def __init__(self, headless, window_width, window_height):
        self.options = []


class FakeDynamicParserType(Enum):
    chrome = FakeDynamicParserTypeChrome
    firefox = FakeDynamicParserTypeFirefox


class TestCreateDynamicParser:
    arguments = ['dynamic_parser_type', 'expectation']
    values = [
        (DynamicParserType.chrome, does_not_raise()),
        (DynamicParserType.firefox, does_not_raise()),
        ('chrome', pytest.raises(UnsupporetdDynamicParserTypeException)),
        (0, pytest.raises(UnsupporetdDynamicParserTypeException)),
        (1.1, pytest.raises(UnsupporetdDynamicParserTypeException)),
        (None, pytest.raises(UnsupporetdDynamicParserTypeException)),
        (FakeDynamicParserType.chrome, pytest.raises(UnsupporetdDynamicParserTypeException)),
        (FakeDynamicParserType.firefox, pytest.raises(UnsupporetdDynamicParserTypeException))
    ]

    @pytest.mark.parametrize(arguments, values)
    def test_create_dynamic_parser(self, dynamic_parser_type, expectation):
        with expectation:
            DynamicParser(dynamic_parser_type)


class TestDynamicParserWork:
    def test_dynamic_parser_open_connection(self):
        # import psutil
        # import datetime

        # def test_check_for_active_process(process_name: str = 'firefox'):
        #     for item in psutil.process_iter():
        #         process = item.as_dict()
        #         if process_name in process['name'] and \
        #                 process['status'] == 'running':
        #             return datetime.datetime.utcfromtimestamp(
        #                 process['create_time']
        #             )

        # dynamic_parser = DynamicParser(
        #     DynamicParserType.firefox, headless=True
        # )
        # dynamic_parser.open_connection()
        # assert (
        #     datetime.datetime.now() - test_check_for_active_process()
        # ).seconds < 100
        pass

    def test_dynamic_parser_get_url(self):
        pass

    def test_dynamic_parser_close_connection(self):
        pass
