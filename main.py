from datetime import date

from calender import Calender
from person import Person
from rule import is_date_after_date, is_date_weekend_after_weekend, is_date_two_days_apart


def main() -> None:
    all_rules = [(is_date_after_date, 100), (is_date_weekend_after_weekend, 80), (is_date_two_days_apart, 85)]

    current_month = 1

    p1 = Person("Nevo", [date(2026, 1, 1), date(2026, 1, 20), date(2026, 1, 30)], all_rules)
    p1.add_time_period_unavailablity(date(2026, 1, 8), date(2026, 1, 17))
    p2 = Person("Shira", [date(2026, 1, 2), date(2026, 1, 20), date(2026, 1, 21)], all_rules)
    p3 = Person("Eidlin", [date(2026, 1, 1)], all_rules)
    p3.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=7)
    p3.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=3)
    p5 = Person("Itay", [date(2026, 1, 1), date(2026, 1, 13), date(2026, 1, 29)], all_rules)
    p5.add_recurring_month_unavailabilities(current_month=current_month, recurring_isoday=3)
    p6 = Person("Nivi", [date(2026, 1, 2)], all_rules)

    my_calender = Calender([p1, p2, p3, p5, p6])
    my_calender.on_calling(current_month)
    my_calender.print_calender()
    for person in my_calender.people:
        print(f"{person.name} on call for {person.get_on_call_amount} days")

if __name__ == "__main__":
    main()