import json
from dataclasses import dataclass, asdict
from datetime import date, timedelta

@dataclass(frozen=True)
class Book:
    isbn: str
    title: str
    author: str

class LendingError(Exception):
    pass

class Library:
    LOAN_DAYS = 14

    def __init__(self):
        self.books = {}
        self.loans = {}

    def add(self, book):
        self.books[book.isbn] = book

    def lend(self, isbn, member, today):
        if isbn not in self.books:
            raise LendingError(f"unknown book {isbn}")
        if isbn in self.loans:
            raise LendingError(f"{isbn} is already on loan")
        due = today + timedelta(days=self.LOAN_DAYS)
        self.loans[isbn] = (member, due)
        return due

    # Add:
    #   overdue(today): a generator yielding (member, title, days_late) for every
    #     loan past its due date, sorted by days_late, most late first
    #   to_json() -> str   and   Library.from_json(text) -> Library (a classmethod)
    #     that round-trip books and loans exactly
