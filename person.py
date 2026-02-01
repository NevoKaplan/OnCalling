from datetime import date, timedelta
from typing import Callable

from rule import is_date_legal_by_calendar_rules, CalendarRule, PersonalRule, is_date_legal_by_personal_rules


class Person:
    def __init__(
            self,
            name: str,
            unavailabilities: list[date],
            personal_rules: list[(Callable[[date | int, date], bool], int)] | None = None
    ):
        self.name = name
        self.unavailabilities = unavailabilities
        self.on_call_dates = []
        self.personal_rules = personal_rules if personal_rules is not None else []

    @property
    def get_on_call_amount(self) -> int:
        return len(self.on_call_dates)

    def add_recurring_month_unavailabilities(self, current_month: int, recurring_isoday: int) -> None:
        current_date = date(year=date.today().year, month=current_month, day=1)

        while current_date.month == current_month:
            if current_date.isoweekday() == recurring_isoday:
                self.unavailabilities.append(current_date)
            current_date += timedelta(days=1)

    def add_time_period_unavailablity(self, start_date: date, end_date: date) -> None:
        current_date = start_date

        while current_date <= end_date:
            self.unavailabilities.append(current_date)
            current_date += timedelta(days=1)

    def add_on_call_date_by_rules(
            self, date_to_add: date, rules: list[CalendarRule], weight_offset: int = 0
    ) -> bool:
        if self.get_on_call_amount >= 1:
            for on_call_date in self.on_call_dates:
                if not is_date_legal_by_calendar_rules(on_call_date, date_to_add, rules, weight_offset):
                    return False
        if not is_date_legal_by_personal_rules(date_to_add, self.personal_rules, weight_offset):
            return False
        self.on_call_dates.append(date_to_add)
        return True

