import random
from datetime import date, timedelta

from exceptions import NoAvailablePersonOnDate
from person import Person

MAX_TRIES = 100

class Calender:
    def __init__(self, people: list[Person]):
        self.people = people
        self.date_to_person = {}


    def print_calender(self):
        for date_key, person in self.date_to_person.items():
            print(f"{str(date_key.strftime("%A, %d-%m-%Y"))} : {person.name if person else "None"}")

    def on_calling(self, current_month: int) -> None:
        for day in _iter_month(month=current_month):
            self.order_people()
            is_date_selected = False

            unavailable_people_count = 0
            weight_offset = 0
            try:

                while not is_date_selected:
                    if unavailable_people_count >= len(self.people):
                        raise NoAvailablePersonOnDate("No people :(", date=day)
                    for person in self.people:
                        if day in person.unavailabilities:
                            unavailable_people_count += 1
                            continue
                        if person.add_on_call_date_by_rules(date_to_add=day, weight_offset=weight_offset):
                            is_date_selected = True
                            self.date_to_person[day] = person
                            break

                        weight_offset += 5

            except NoAvailablePersonOnDate:
                self.date_to_person[day] = None
                continue



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
