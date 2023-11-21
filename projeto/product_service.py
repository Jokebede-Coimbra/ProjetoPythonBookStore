from product import Product
from product_image_interface import ProductImageInterface
from product_repository_interface import ProductRepositoryInterface
        
class ProductService:
    def __init__(self, product_image_interface: ProductImageInterface, product_repository_interface: ProductRepositoryInterface) -> None:
        self.product_image_interface = product_image_interface
        self.product_repository_interface = product_repository_interface
 
  
    def create_product(self, product: Product):
        
        self.product_repository_interface.append_product(product)
        self.product_image_interface.put_product_file(product.id, product.image)
        return "Product created successfully!"
    def update_product(self, id: str, updated_product: Product):
       
        if self.product_repository_interface.update_product(id, updated_product):
            self.product_image_interface.replace_product_file(id, updated_product.image)
            return True
        return None

    def delete_product(self, id: str):
        
        if self.product_repository_interface.delete_product(id):
            self.product_image_interface.remove_product_file(id)
            return True
        return None
