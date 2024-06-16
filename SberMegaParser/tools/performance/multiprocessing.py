from typing import Callable, Iterable
from threading import Thread
import pandas as pd
import os
from SberMegaParser.tools.dataframes.dataframes import (
    read_dataframe, save_dataframe, create_empty_dataframe
)
from SberMegaParser.core import (StaticParser, DynamicParser, Parser)
from SberMegaParser.core.factories import (DynamicParserFactory, StaticParserFactory)

__all__ = ['multi_parser']


def multi_parser(
    dataframe_input_path,
    dataframe_output_path: str,
    logic: Callable,
    proxy = None,
    cookies = None,
    user_agents = None,
    threads_count: int = 1,
    is_dynamic: bool = True,
):
    # TODO: заимпортировать отдельные модули из os как закончим
    # первичная валидация
    df_input = None
    df_input_splits = None
    result = None

    # TODO: под удаление
    if not isinstance(threads_count, int):
        raise ValueError('Количество потоков должно быть целочисленным')

    if dataframe_input_path:
        if not os.path.isfile(dataframe_input_path):
            raise ValueError('Входной файл не существует')
        df_input = read_dataframe(dataframe_input_path)

    if not os.path.isdir(os.path.dirname(dataframe_output_path)):
        raise ValueError('Путь для сохранения файлов не существует')
    if df_input:
        df_input_splits = _split_data_frame(df_input, threads_count)

    factory = DynamicParserFactory() if is_dynamic else StaticParserFactory()

    # logic должен кушать парсер на входе (причем лучше взять класс Parser)

    threads = []
    for i in range(threads_count):
        threads.append(Thread(target=logic,
                              args=(factory.create(), )))
    # TODO: + еще должен кушать список url-ов
    # TODO: + сделать контроль append dataframe в список

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # заглушка (типа полученные спаршенные порции данных)
    df_output_splits = [create_empty_dataframe(['A', 'B', 'C'])
                        for i in range(threads_count)]

    df_output = _merge_data_frames(df_output_splits)

    save_dataframe(df_output, dataframe_output_path)


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
