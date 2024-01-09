from typing import List
from entities.product import Product
from interfaces.product_repository_interface import ProductRepositoryInterface


class ProductMemoryRepository(ProductRepositoryInterface):
    
    def __init__(self) -> None:
        self.products: list[Product] = []

    def append(self, product: Product) -> None:
        self.products.append(product)

    def update(self, id: str, product: Product) -> bool:
        for i, product in enumerate(self.products):
            if product.id == id:
                self.products[i] = product
                return True

        return False

    def get(self) -> List[Product]:
        return self.products
        
    def get_by_id(self, id: str) -> Product:
        for product in self.products:
            if product.id == id:
                return product

        return None
    
    def delete(self, id: str) -> bool:
        for i, product in enumerate(self.products):
            if product.id == id:
                del self.products[i]
                return True
        return False