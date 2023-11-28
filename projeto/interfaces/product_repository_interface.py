from abc import ABC, abstractmethod

from entities.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def append(self, product: Product) -> None:
        pass

    @abstractmethod
    def update(self, id: str, product: Product) -> bool:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass