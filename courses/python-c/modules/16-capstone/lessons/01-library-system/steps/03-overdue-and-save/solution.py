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

    def overdue(self, today):
        late = []
        for isbn, (member, due) in self.loans.items():
            if due < today:
                late.append((member, self.books[isbn].title, (today - due).days))
        late.sort(key=lambda row: -row[2])
        yield from late

    def to_json(self):
        return json.dumps({
            "books": [asdict(b) for b in self.books.values()],
            "loans": {isbn: [m, due.isoformat()] for isbn, (m, due) in self.loans.items()},
        })

    @classmethod
    def from_json(cls, text):
        data = json.loads(text)
        lib = cls()
        for b in data["books"]:
            lib.add(Book(**b))
        for isbn, (member, due) in data["loans"].items():
            lib.loans[isbn] = (member, date.fromisoformat(due))
        return lib
