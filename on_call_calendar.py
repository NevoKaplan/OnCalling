import random
from datetime import date, timedelta

from exceptions import NoAvailablePersonOnDate
from person import Person

class OnCallCalendar:
    def __init__(self, people: list[Person]):
        self.people = people
        self.date_to_person = {}


    def print_calender(self):
        for date_key, person in self.date_to_person.items():
            print(f"{str(date_key.strftime("%A, %d-%m-%Y"))} : {person.name if person else "None"}")

    def on_calling(self, current_month: int) -> None:
        for day in _iter_month(month=current_month):
            self.order_people()
            try:
                self.select_date(day)
            except NoAvailablePersonOnDate:
                self.date_to_person[day] = None
                continue


    def select_date(self, day: date) -> None:
        weight_offset = 0
        unavailable_people_count = 0
        is_date_selected = False

        while not is_date_selected:
            if unavailable_people_count >= len(self.people):
                raise NoAvailablePersonOnDate("No people :(", date=day)
            for person in self.people:
                if day in person.unavailabilities:
                    unavailable_people_count += 1
                    continue
                if person.add_on_call_date_by_rules(
                        date_to_add=day, weight_offset=(weight_offset + len(person.unavailabilities))
                ):
                    self.date_to_person[day] = person
                    is_date_selected = True
                    break

                weight_offset += 5


    def order_people(self) -> None:
        random.shuffle(self.people)
        self.people.sort(key=lambda person: person.get_on_call_amount)


def _iter_month(month: int, year: int = date.today().year):
    start = date(year, month, 1)

    if month == 12:
        end = date(year + 1, 1, 1)
    else:
        end = date(year, month + 1, 1)

    current = start
    while current < end:
        yield current
        current += timedelta(days=1)

def get_people_on_call_biggest_diff(calender: OnCallCalendar) -> int:
    if len(calender.people) < 2:
        return 0

    on_call_for = [person.get_on_call_amount for person in calender.people]
    return max(on_call_for) - min(on_call_for)

def select_most_equal_calendar(calenders: list[OnCallCalendar]) -> OnCallCalendar:
    return min(calenders, key=get_people_on_call_biggest_diff)
