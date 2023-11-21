from io import BytesIO

from entities.product import Product
from interfaces.product_image_interface import ProductImageInterface
from interfaces.product_repository_interface import ProductRepositoryInterface


class ProductService:
    def __init__(self, product_repository_interface: ProductRepositoryInterface, product_image_interface: ProductImageInterface) -> None:
        self.product_repository_interface = product_repository_interface
        self.product_image_interface = product_image_interface

    def create(self, product: Product, image: BytesIO):
        self.product_repository_interface.append_product(product)
        self.product_image_interface.put_product_file(
            product.file_name, image)

        return f"Product {product.id} - {product.name} created successfully!"

    def update(self, id: str, updated_product: Product):
        if self.product_repository_interface.update_product(id, updated_product):
            self.product_image_interface.replace_product_file(
                id, updated_product.file_name)
            return True

        return None

    def delete(self, id: str):
        if self.product_repository_interface.delete_product(id):
            self.product_image_interface.remove_product_file(id)
            return True

        return None
