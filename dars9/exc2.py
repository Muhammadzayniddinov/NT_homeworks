from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
import datetime


class AbstractUser(ABC):
    @abstractmethod
    def borrow_book(self, book) -> None:
        pass

    @abstractmethod
    def return_book(self, book) -> None:
        pass

class AbstractBook(ABC):
    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass

    @abstractmethod
    def get_isbn(self) -> str:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def set_status(self, status) -> None:
        pass

class AbstractLibrary(ABC):
    @abstractmethod
    def add_book(self, book) -> None:
        pass

    @abstractmethod
    def remove_book(self, book) -> None:
        pass

    @abstractmethod
    def find_book(self, query) -> List:
        pass


class Status(Enum):
    AVAILABLE = "Available"
    NOT_AVAILABLE = "Not Available"


@dataclass
class Book(AbstractBook):
    title: str
    author: str
    isbn: str
    status: Status = Status.AVAILABLE
    due_time: Optional[datetime.date] = None

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_isbn(self) -> str:
        return self.isbn

    def get_status(self) -> str:
        return self.status.value

    def set_status(self, status: Status) -> None:
        self.status = status


@dataclass
class Library(AbstractLibrary):
    books: List[Book] = field(default_factory=list)
    
    def add_book(self, book: Book):
        self.books.append(book)
        print(f'{book.get_title()} kitobi kutubxonaga qo\'shildi.')

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f'{book.get_title()} kitobi kutubxonadan olib tashlandi.')
        else:
            print(f'{book.get_title()} kitobi kutubxonada mavjud emas.')

    def find_book(self, query) -> List[Book]:
        return [book for book in self.books if
                query.lower() in book.get_title().lower() or
                query.lower() in book.get_author().lower() or
                query in book.get_isbn()]

@dataclass
class User(AbstractUser):
    name: str
    member_id: str
    borrowed_books: List[Book] = field(default_factory=list)

    def borrow_book(self, book: Book, days=14):
        if book.get_status() == Status.AVAILABLE.value:
            book.set_status(Status.NOT_AVAILABLE)
            book.due_time = datetime.datetime.now().date() + datetime.timedelta(days=days)
            self.borrowed_books.append(book)
            print(f'{self.name} ga {book.get_title()} kitobi {book.due_time} vaqtgacha berildi.')
        else:
            print(f'{book.get_title()} kitobi mavjud emas. {book.due_time + datetime.timedelta(days=1)} sanada olib ketishingiz mumkin.')

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_status(Status.AVAILABLE)
            book.due_time = None
            print(f'{book.get_title()} kitobi kutubxonaga qaytarildi.')
        else:
            print(f'{book.get_title()} kitobi qarzga berilmagan.')

library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789")
book2 = Book("1984", "George Orwell", "987654321")
user1 = User("Alice", "P001")

library.add_book(book1)
library.add_book(book2)

user1.borrow_book(book1)

for book in user1.borrowed_books:
    print(f'{user1.name} a\'zosining qarzga olingan kitobi: {book.get_title()}')
