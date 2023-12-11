from io import BytesIO
from typing import List

from entities.product import Product
from interfaces.product_image_interface import ProductImageInterface
from interfaces.product_repository_interface import ProductRepositoryInterface


class ProductService:
    def __init__(self, product_repository_interface: ProductRepositoryInterface, product_image_interface: ProductImageInterface) -> None:
        self.product_repository_interface = product_repository_interface
        self.product_image_interface = product_image_interface

    def create(self, product: Product, image: BytesIO):
        self.product_repository_interface.append(product)
        self.product_image_interface.put(
            product.file_name, image)

        return f"Product {product.id} - {product.name} created successfully!"

    def update(self, id: str, updated_product: Product, updated_image: BytesIO):
        if self.product_repository_interface.update(id, updated_product):
            self.product_image_interface.replace(
               updated_product.file_name, updated_image)
            return True

        return None
    
    def get (self) -> List[Product]:
        return self.product_repository_interface.get()
    
    def get_by_id(self, id: str) -> Product:
        return self.product_repository_interface.get_by_id(id)
            
    def delete(self, id: str) -> bool:
        product = self.product_repository_interface.get_by_id(id)
        if product:
            self.product_repository_interface.delete(id)
            self.product_image_interface.remove(product.file_name)
            return True

        return False