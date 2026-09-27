from dataclasses import dataclass
from datetime import date, timedelta

# Write:
#   Book: frozen dataclass (isbn: str, title: str, author: str)
#   LendingError(Exception)
#   Library with:
#     add(book)
#     lend(isbn, member, today) -> due date (today + 14 days)
#         raises LendingError if the isbn is unknown or already lent
#     give_back(isbn)  raises LendingError if it was not lent
#     available() -> list of titles not on loan, sorted
