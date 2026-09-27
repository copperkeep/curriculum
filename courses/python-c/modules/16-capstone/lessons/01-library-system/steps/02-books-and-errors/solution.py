from dataclasses import dataclass
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

    def give_back(self, isbn):
        if isbn not in self.loans:
            raise LendingError(f"{isbn} is not on loan")
        del self.loans[isbn]

    def available(self):
        return sorted(b.title for isbn, b in self.books.items() if isbn not in self.loans)
