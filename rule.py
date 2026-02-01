import random
from datetime import date, timedelta
from typing import Callable

CalendarRule = Callable[[date, date], bool]
PersonalRule = Callable[[int, date], bool]

def is_date_legal_by_calendar_rules(
        first_date: date,
        second_date: date,
        condition_list: list[(CalendarRule, int)],
        weight_offset: int = 0
) -> bool:
    for calendar_rule, weight in condition_list:
        if calendar_rule(first_date, second_date) and random.randint(1, 100) <= (weight - weight_offset):
                return False
    return True

def is_date_legal_by_personal_rules(
        date_to_add: date,
        condition_list: list[(PersonalRule, int)],
        weight_offset: int = 0
) -> bool:
    for personal_rule, weight in condition_list:
        if personal_rule(date_to_add) and random.randint(1, 100) <= (weight - weight_offset):
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

def is_date_less_desired_weekday(unwanted_isodate: int, second_date: date) -> bool:
    """Args:
        unwanted_isodate (int): The `less desired` day of the week (Monday == 1, Sunday == 7).
        second_date (date): The current date.
    """

    return unwanted_isodate == second_date.isoweekday()
