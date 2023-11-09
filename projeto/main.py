from book import Book
from product_repository_interface import ProductRepositoryInterface
from product_memory_repository import ProductMemoryRepository


product_memory_repository = ProductMemoryRepository()

product1 = ProductMemoryRepository("1", "XX1", "XXXX11", "Autor X", '4', 25.98)

product_memory_repository.append(product1)