import datetime
from enum import Enum
from dataclasses import dataclass, field
from typing import List

class Status(Enum):
    AVAILABLE = "Available"
    NOT_AVAILABLE = "Not Available"

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: Status = Status.AVAILABLE
    due_time: datetime.date = None

@dataclass
class Patron:
    name: str
    member_id: str
    borrowed_books: List[Book] = field(default_factory=list)

@dataclass
class Library:
    books: List[Book] = field(default_factory=list)
    patrons: List[Patron] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books.append(book)
        print(f'{book.title} kitobi kutubxonaga qo\'shildi.')

    def add_patron(self, patron: Patron):
        self.patrons.append(patron)
        print(f'{patron.name} kutubxonaga qo\'shildi')

    def borrow_book(self, book: Book, patron: Patron, days=14) -> None:
        if book.status == Status.AVAILABLE:
            book.status = Status.NOT_AVAILABLE
            book.due_time = datetime.datetime.now().date() + datetime.timedelta(days=days)
            patron.borrowed_books.append(book)
            print(f'{patron.name} ga {book.title} kitobi {book.due_time} vaqtgacha berildi.')
        else:
            print(f'{book.title} kitobi mavjud emas. {book.due_time + datetime.timedelta(days=1)} sanada olib ketishingiz mumkin.')

    def return_book(self, book: Book, patron: Patron):
        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.status = Status.AVAILABLE
            book.due_time = None
            print(f'{book.title} kitobi kutubxonaga qaytarildi.')
        else:
            print(f'{book.title} kitobi qarzga berilmagan.')

    def search_books(self, query):
        return [book for book in self.books if
                query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or
                query in book.isbn]

    def display_borrowed_books(self, patron: Patron = None):
        if patron:
            return patron.borrowed_books
        else:
            borrowed_books = {}
            for patron in self.patrons:
                borrowed_books[patron.member_id] = patron.borrowed_books
            return borrowed_books

library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")
patron1 = Patron("Alice", "P001")

library.add_book(book1)
library.add_book(book2)
library.add_patron(patron1)

library.borrow_book(book1, patron1)

borrowed_books = library.display_borrowed_books()
for member_id, books in borrowed_books.items():
    print(f'{member_id} a\'zosining qarzga olingan kitoblari:')
    for book in books:
        print(f' - {book.title}')

print(book2.status)
