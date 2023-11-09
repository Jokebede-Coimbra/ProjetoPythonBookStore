from abc import ABC, abstractmethod
from book import Book

class ProductRepositoryInterface(ABC):
    
    @abstractmethod
    def append_book(self, book: Book) -> None:
        pass
    @abstractmethod
    def update_book(self, id, book: Book) -> None:
        pass
    @abstractmethod
    def delete_book(self, id, book: Book) -> None:
        pass
