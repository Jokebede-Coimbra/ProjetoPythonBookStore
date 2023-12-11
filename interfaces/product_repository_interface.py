from abc import ABC, abstractmethod
from typing import List

from entities.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def append(self, product: Product) -> None:
        pass

    @abstractmethod
    def update(self, id: str, product: Product) -> bool:
        pass

    @abstractmethod
    def get(self) -> List[Product]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: str) -> Product:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> bool:
        pass