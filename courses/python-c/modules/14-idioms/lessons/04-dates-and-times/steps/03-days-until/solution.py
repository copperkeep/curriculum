from datetime import date

def days_until_birthday(today, month, day):
    next_bday = date(today.year, month, day)
    if next_bday < today:
        next_bday = date(today.year + 1, month, day)
    return (next_bday - today).days
