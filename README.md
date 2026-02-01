# OnCalling
Project for selected people to stay `on call` after work during the week.

## Adding a person
### Examples:

---
A person with unavailabilities at the first day of the month and on his birthday:
```python 
person = Person("Nevo", [date(2026, 12, 1), date(2026, 12, 22)])
```
---
The same person with a personal rule:
- This personal rule means that the person has a 65% chance to not get thursdays.
```python 
personal_rules = [(partial(is_date_less_desired_weekday, 4), 65)]
person = Person("Nevo", [date(2026, 12, 1), date(2026, 12, 2)], personal_rules)
```
---
The same person but he's not available for a couple of days in a row:
```python
person = Person("Nevo", [date(2026, 12, 1), date(2026, 12, 2)])
person.add_time_period_unavailablity(date(2026, 12, 20), date(2026, 12, 24))
```
---
The same person but he can't on sundays:
```python
person = Person("Nevo", [date(2026, 12, 1), date(2026, 12, 2)])
person.add_recurring_month_unavailabilities(current_month=12, recurring_isoday=7)
```
---
### Hopefully you'd be able to figure the rest out by yourselves.
