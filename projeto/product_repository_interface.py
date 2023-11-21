from abc import ABC, abstractmethod
from product import Product

class ProductRepositoryInterface(ABC):
    
    @abstractmethod
    def append_product(self, product: Product) -> None:
        pass
    @abstractmethod
    def update_product(self, id, product: Product) -> None:
        pass
    @abstractmethod
    def delete_product(self, id, product: Product) -> None:
        pass