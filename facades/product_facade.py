from io import BytesIO
from typing import List

from entities.product import Product
from services.product_service import ProductService


class ProductFacade:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def create(self, product: Product, image: BytesIO):
        return self.product_service.create(product, image)

    def update(self, id, up_product: Product, updated_image: BytesIO):
        return self.product_service.update(id, up_product, updated_image)
    
    def get(self) -> List[Product]:
        return self.product_service.get()
    
    def get_by_id(self, id: str):
        return self.product_service.get_by_id(id)
        
    def delete(self, id: str):
        return self.product_service.delete(id)
          