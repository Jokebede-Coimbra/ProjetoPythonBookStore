from book import Book
from product_repository_interface import ProductRepositoryInterface
from book_repository import BookRepository

book_repository = BookRepository()

book1 = Book("1","Harry Potter", "J.K. Rowling", "Jkbd", "5", 29.99)
book2 = Book("2","Lord of the Rings", "J.R.R. Tolkien", "Well", "4.5", 19.99)

book_repository.append_book(book1)
book_repository.append_book(book2)

print("Livros no repositório:")

for book in book_repository.books:
    print(f"{book.id}: {book.title} - {book.author} - {book.name} - {book.rating} - {book.price}")
# ===================================================================
update_success = book_repository.update_book("1", Book("1", "New Title", "New ISBN", "New Author", "5", 30.0))
if update_success:
    print("Livro atualizado com sucesso!")
else:
    print("Falha ao atualizar o livro. Livro não encontrado.")

# ===================================================================
delete_success = book_repository.delete_book("1")
if delete_success:
    print("Livro excluído com sucesso!")
else:
    print("Falha ao excluir o livro. Livro não encontrado.")