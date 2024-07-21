import pytest
from contextlib import nullcontext as does_not_raise
import pandas as pd
from MegaParser import (
    read_dataframe, save_dataframe, create_empty_dataframe
)
from MegaParser import UnsupporetdFileExtensionException


class TestCreateEmptyDataFrame:
    args = ['columns', 'excpectation']
    vals = [
        (['first', 'second', 3], pytest.raises(TypeError)),
        ([1, 2, 3],              pytest.raises(TypeError)),
        (123,                    pytest.raises(TypeError)),
        (['first', 'second'],    does_not_raise()),
        (('first', 'second'),    does_not_raise())
    ]

    def test_create_empty_dataframe_result_type(self):
        assert type(create_empty_dataframe(['first', 'second'])) == pd.DataFrame

    def test_create_empty_dataframe_result_len(self):
        assert len(create_empty_dataframe(('first', 'second'))) == 0

    def test_create_empty_dataframe_result_columns(self):
        assert list(create_empty_dataframe(['first', 'second']).columns) == \
            ['first', 'second']

    @pytest.mark.parametrize(args, vals)
    def test_create_empty_dataframe_exceptions(self, columns, excpectation):
        with excpectation:
            assert create_empty_dataframe(columns)


class TestReadData:
    args = ['file_path', 'expectation']
    vals = [
        ('pytest.ini', pytest.raises(UnsupporetdFileExtensionException))
    ]

    @pytest.mark.parametrize(args, vals)
    def test_read_data_exceptions(self, file_path, expectation):
        with expectation:
            read_dataframe(file_path)


# class TestSaveData:
#     args = ['file_path', 'expectation']
#     vals = [
#         ('pytest.ini', pytest.raises(UnsupporetdFileExtensionException))
#     ]

#     @pytest.mark.parametrize(args, vals)
#     def test_save_data_exceptions(self, file_path, expectation):
#         with expectation:
#             save_dataframe(file_path)
