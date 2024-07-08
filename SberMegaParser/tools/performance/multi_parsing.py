import warnings
from typing import Callable, Iterable
from threading import Thread
import pandas as pd
import os
from SberMegaParser.tools.dataframes.dataframes import (
    read_dataframe, save_dataframe, create_empty_dataframe
)
from SberMegaParser.tools.user_agents import *
from SberMegaParser.tools.performance.multiprocessor import Multiprocessor
from SberMegaParser.core.factories import *

__all__ = ['multi_parser']


def multi_parser(
    dataframe_input_path: str | None,
    dataframe_output_path: str,
    logic: Callable,
    proxy_list=None,
    cookies_list=None,
    user_agents_list=None,
    threads_count: int = 1,
    is_dynamic: bool = True,
    generate_user_agents=True
):
    # TODO: заимпортировать отдельные модули из os как закончим
    # первичная валидация
    df_input = None
    df_input_splits = []
    df_output_splits = []
    result = None

    # TODO: переработать после дебага
    if dataframe_input_path:
        if not os.path.isfile(dataframe_input_path):
            raise ValueError('Входной файл не существует')
        df_input = read_dataframe(dataframe_input_path)

    if df_input is not None:
        df_input_splits = _split_data_frame(df_input, threads_count)

    if not os.path.isdir(os.path.dirname(dataframe_output_path)):
        raise ValueError('Путь для сохранения файлов не существует')

    if user_agents_list and generate_user_agents:
        warnings.warn(
            'Нельзя генерировать новые User Agent поверх существующих.'
            'Флаг generate_user_agents будет проигнорирован.')
    elif not user_agents_list and generate_user_agents:
        user_agents_list = [generate_user_agent(
            browsers=[UserAgentBrowsers.CHROME, UserAgentBrowsers.FIREFOX],
            operating_systems=UserAgentOperatingSystems.WINDOWS,
            platforms=UserAgentPlatforms.PC)
            for _ in range(threads_count)]

    factory = DynamicParserFactory(user_agents=user_agents_list) if is_dynamic \
        else StaticParserFactory()

    mp = Multiprocessor()
    for i, new_parser in enumerate(factory.get_parsers()):
        mp.run(logic, parser=new_parser, urls=df_input_splits[i])

    df_output_splits = mp.wait()

    # заглушка (типа полученные спаршенные порции данных)
    # df_output_splits = [create_empty_dataframe(['A', 'B', 'C'])
    #                    for _ in range(threads_count)]

    df_output = _merge_data_frames(df_output_splits)

    save_dataframe(df_output, dataframe_output_path)


def _split_data_frame(df: pd.DataFrame, parts_count: int) -> Iterable[
    pd.DataFrame]:
    part_length = round(len(df) / parts_count)
    splits = [df[part_length * offset: part_length * (offset + 1)]
              for offset in range(parts_count)]
    return splits


def _merge_data_frames(df_collection: Iterable[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(list(df_collection))
