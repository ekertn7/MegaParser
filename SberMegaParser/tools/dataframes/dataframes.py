from typing import Iterable
import pandas as pd
from SberMegaParser.exceptions import (
    UnsupporetdFileExtensionException
)

__all__ = ['create_empty_dataframe', 'read_dataframe', 'save_dataframe']


EXCEL_ENGINE = 'openpyxl'
EXCEL_EXTENSIONS = ['xlsx', 'xls']
CSV_ENCODING = 'utf-8'
CSV_SEPARATOR = ','
CSV_EXTENSIONS = ['cvs', 'txt']


def create_empty_dataframe(columns: list[str] | tuple[str]) -> pd.DataFrame:
    if all(isinstance(elem, str) for elem in columns) and \
            isinstance(columns, (list, tuple)):
        return pd.DataFrame(columns=columns, data=[])
    else:
        raise TypeError()


def _compare_file_extension(
    file_name: str,
    file_extension: Iterable[str] | str
) -> bool:
    return file_name.split('.')[-1] in file_extension


def read_dataframe(
    file_path: str,
    separator: str = CSV_SEPARATOR,
    encoding: str = CSV_ENCODING,
    excel_engine: str = EXCEL_ENGINE
) -> pd.DataFrame:
    if _compare_file_extension(file_path, EXCEL_EXTENSIONS):
        result = pd.read_excel(
            file_path,
            dtype='str',
            engine=excel_engine
        )
    elif _compare_file_extension(file_path, CSV_EXTENSIONS):
        result = pd.read_csv(
            file_path,
            dtype='str',
            sep=separator,
            encoding=encoding
        )
    else:
        raise UnsupporetdFileExtensionException(
            supported_file_extensions=EXCEL_EXTENSIONS+CSV_EXTENSIONS
        )
    return result


def save_dataframe(
    df: pd.DataFrame,
    file_path: str,
    separator: str = CSV_SEPARATOR,
    encoding: str = CSV_ENCODING,
    excel_engine: str = EXCEL_ENGINE,
    index_label: str = None
) -> None:
    if _compare_file_extension(file_path, EXCEL_EXTENSIONS):
        df.to_excel(
            file_path,
            index=True if index_label else False,
            index_label=index_label,
            engine=excel_engine
        )
    elif _compare_file_extension(file_path, CSV_EXTENSIONS):
        df.to_csv(
            file_path,
            index=True if index_label else False,
            index_label=index_label,
            sep=separator,
            encoding=encoding
        )
    else:
        raise UnsupporetdFileExtensionException(
            supported_file_extensions=EXCEL_EXTENSIONS+CSV_EXTENSIONS
        )
