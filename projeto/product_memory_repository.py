from book import Book
from product_repository_interface import ProductRepositoryInterface

class ProductMemoryRepository(ProductRepositoryInterface):
    
    def __init__(self) -> None:
      self.books: list[Book] = []
      
    def insert_book(self, book: Book) -> None:
       self.books.append(book)
       
    def update_book(self, id:str, book: Book) -> None:
        self.books[id] = book
    
    def delete_book(self, id:str) -> None:
        self.books[id]