import pytest
from contextlib import nullcontext as does_not_raise
from SberMegaParser import multi_parser
from SberMegaParser.tools.performance.multiprocessing import (
    _split_data_frame, _merge_data_frames
)


class TestMultiParser:
    args = [
        'dataframe_input_path', 'dataframe_output_path', 'logic',
        'proxy', 'cookies', 'user_agents', 'threads_count', 'expectation'
    ]
    vals = [
        (None, None, None, None, None, None, None, does_not_raise()),
    ]

    @pytest.mark.parametrize(args, vals)
    def test_multi_parser_exceptions(
        self, dataframe_input_path, dataframe_output_path, logic, proxy,
        cookies, user_agents, threads_count, expectation
    ):
        with expectation:
            multi_parser(
                dataframe_input_path, dataframe_output_path, logic, proxy,
                cookies, user_agents, threads_count
            )


class TestDataFrameProcessing:
    def test_split_data_frame(self):
        input_data = ...
        parts_count = 2
        output_data = [...]
        assert _split_data_frame(input_data, parts_count) == output_data

    def test_couple_data_frames(self):
        input_data = [...]
        output_data = ...
        assert _merge_data_frames(input_data) == output_data
