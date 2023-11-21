from entities.product import Product
from interfaces.product_repository_interface import ProductRepositoryInterface


class ProductDynamoDbRepository(ProductRepositoryInterface):
    def __init__(self) -> None:
        self.products: list[Product] = []

    def append_product(self, product: Product) -> None:
        self.products.append(product)

    def update_product(self, id: str, product: Product) -> None:
        for product in self.products:
            if product.id == id:
                return product

        return None

    def delete_product(self, id: str) -> None:
        if id in self.products:
            del self.products[id]
        return False
