from typing import Callable, Iterable
import pandas as pd
import os
from SberMegaParser.tools.dataframes.dataframes import (
    read_dataframe, save_dataframe, create_empty_dataframe
)

__all__ = ['multi_parser']


def multi_parser(
    dataframe_input_path: str,
    dataframe_output_path: str,
    logic: Callable,
    proxy,
    cookies,
    user_agents,
    threads_count: int = 1,
    dynamic: bool = True,
):

    # TODO: заимпортировать отдельные модули из os как закончим
    # первичная валидация
    df_input = None
    df_input_splits = None

    if not isinstance(threads_count, int):
        raise ValueError('Количество потоков должно быть целочисленным')

    if dataframe_input_path:
        if not os.path.isfile(dataframe_input_path):
            raise ValueError('Входной файл не существует')
        # TODO: кастомизироать чтение в зависимости от типа
        df_input = pd.read_csv(dataframe_input_path)

    if not os.path.isdir(os.path.dirname(dataframe_output_path)):
        raise ValueError('Путь для сохранения файлов не существует')

    if df_input:
        df_input_splits = _split_data_frame(df_input, threads_count)


def _split_data_frame(df: pd.DataFrame, parts_count: int) -> Iterable[
    pd.DataFrame]:
    # вопрос - делим рандомно или последовательно по индексу?
    # пока пусть будет последовательно
    part_length = round(len(df) / parts_count)
    splits = [df[part_length * offset : part_length * (offset + 1)]
              for offset in range(parts_count)]
    return splits


def _merge_data_frames(df_collection: Iterable[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(list(df_collection))
