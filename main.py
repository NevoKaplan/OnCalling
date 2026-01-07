import copy
from datetime import date

import pandas

from calender import Calender, select_most_equal_calendar
from person import Person
from rule import is_date_after_date, is_date_weekend_after_weekend, is_date_two_days_apart

def read_data() -> None:
    CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ1MQmxxx4ofMtLy5Ijotpc3Tr4RB7_1v7A4n41cb59UBITZNbER0KoFtg0qM2wL9wc9ndY-SfWIyAo/pub?output=csv"
    clients_df = pandas .read_csv(CSV_URL)


def post_data(my_calender: Calender) -> None:
    WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyamzsEusJQucvtEn5leXxRbzsXPIOzyzsqWet68VPxkxtiIfFomfGHmTQf359EZsg/exec"


def main() -> None:
    all_rules = [(is_date_after_date, 90), (is_date_weekend_after_weekend, 80), (is_date_two_days_apart, 75)]

    current_month = 1

    p1 = Person("Ne", [date(2026, 1, 1), date(2026, 1, 20), date(2026, 1, 30)], all_rules)
    p1.add_time_period_unavailablity(date(2026, 1, 8), date(2026, 1, 17))
    p2 = Person("Sh", [date(2026, 1, 2), date(2026, 1, 20), date(2026, 1, 21)], all_rules)
    p3 = Person("Ei", [date(2026, 1, 1)], all_rules)
    p3.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=7)
    p3.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=3)
    p5 = Person("It", [date(2026, 1, 1), date(2026, 1, 13), date(2026, 1, 29)], all_rules)
    p5.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=3)
    p6 = Person("Ni", [date(2026, 1, 2)], all_rules)

    people = [p1, p2, p3, p5, p6]
    calendars = []
    for i in range(5):
        my_calender = Calender(copy.deepcopy(people))
        my_calender.on_calling(current_month)
        calendars.append(my_calender)

    best_calender = select_most_equal_calendar(calendars)
    best_calender.print_calender()
    for person in best_calender.people:
        print(f"{person.name} on call for {person.get_on_call_amount} days")

if __name__ == "__main__":
    main()