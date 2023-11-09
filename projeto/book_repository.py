from book import Book
from product_repository_interface import ProductRepositoryInterface

class BookRepository(ProductRepositoryInterface):

    def __init__(self) -> None:
      self.books: list[Book] = []
      
    def append_book(self, book: Book) -> None:
       self.books.append(book)
       
    def update_book(self, id:str, book: Book) -> None:
        if id in self.books:
            self.books[id] = book
            return True
        return False
    
    def delete_book(self, id:str) -> None:
        if id in self.books:
            del self.books[id]
        return False