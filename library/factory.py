from abc import ABC, abstractmethod
from .book import Book
from .loan import Loan

# Factory Method
class LibraryFactory(ABC):
    @abstractmethod
    def create_book(self, title: str, author: str, copies: int) -> Book:
        pass

    @abstractmethod
    def create_loan(self, book: Book) -> Loan:
        pass

class ConcreteLibraryFactory(LibraryFactory):
    def create_book(self, title: str, author: str, copies: int) -> Book:
        return Book(title, author, copies)

    def create_loan(self, book: Book) -> Loan:
        return Loan(book)
