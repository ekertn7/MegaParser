from typing import Callable, Iterable
import pandas as pd
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
):
    pass


def _split_data_frame(df: pd.DataFrame, parts_count: int) -> Iterable[pd.DataFrame]:
    pass


def _couple_data_frames(df: Iterable[pd.DataFrame]) -> pd.DataFrame:
    pass
