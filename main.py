import copy
from datetime import date
from functools import partial

from on_call_calendar import OnCallCalendar, select_most_equal_calendar
from person import Person
from rule import is_date_after_date, is_date_weekend_after_weekend, is_date_two_days_apart, is_date_less_desired_weekday


def main() -> None:
    all_calendar_rules = [(is_date_after_date, 90), (is_date_weekend_after_weekend, 80), (is_date_two_days_apart, 75)]
    personal_eid_rules = [(partial(is_date_less_desired_weekday, 4), 65)]

    current_month = date.today().month  # Can also be a number for future months...

    p1 = Person("Ne", [date(2026, current_month, 19)])
    p1.add_time_period_unavailablity(date(2026, current_month, 2), date(2026, current_month, 10))
    p2 = Person("Sh", [])
    p2.add_time_period_unavailablity(date(2026, current_month, 2), date(2026, current_month, 10))
    p3 = Person("Ei", [date(2026, current_month, 3), date(2026, current_month, 4), date(2026, current_month, 14)], personal_eid_rules)
    p3.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=7)
    p4 = Person("Ni", [date(2026, current_month, 19)])
    p4.add_time_period_unavailablity(date(2026, current_month, 5), date(2026, current_month, 9))

    people = [p1, p2, p3, p4]
    calendars = []
    for i in range(5):
        my_calender = OnCallCalendar(copy.deepcopy(people), all_calendar_rules)
        my_calender.on_calling(current_month)
        calendars.append(my_calender)

    best_calender = select_most_equal_calendar(calendars)
    best_calender.print_calender()
    for person in best_calender.people:
        print(f"{person.name} on call for {person.get_on_call_amount} days")

if __name__ == "__main__":
    main()