import random
from datetime import date, timedelta
from typing import Callable


def is_date_legal(
        first_date: date,
        second_date: date,
        condition_list: list[(Callable[[date, date], bool], int)],
        weight_offset: int = 0
) -> bool:
    for func, weight in condition_list:
        if func(first_date, second_date) and random.randint(1, 99) <= (weight - weight_offset):
                return False
    return True

def is_date_after_date(first_date: date, second_date: date) -> bool:
    return abs(first_date - second_date) == timedelta(days=1)

def is_date_two_days_apart(first_date: date, second_date: date) -> bool:
    return abs(first_date - second_date) == timedelta(days=2)

def is_date_weekend_after_weekend(first_date: date, second_date: date) -> bool:
    weekend = [5, 6]

    if first_date.isoweekday() in weekend:
        return abs(first_date - second_date) in [timedelta(days=7), timedelta(days=8)]

    return False
