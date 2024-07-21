import time
import random
from typing import Tuple
from collections import namedtuple

__all__ = ['sleep_random', 'TimeRange']


TimeRange = namedtuple('TimeRange', ('range_from', 'range_to'))


def sleep_random(
    sleep_range: Tuple[int, int] | TimeRange
) -> None:
    """Sleep function in random range.

    Parameters
    ----------
    sleep_range
        Time range within which time is selected randomly.
        Values in milliseconds.
    """
    time.sleep(random.randint(*sleep_range)/1000)
