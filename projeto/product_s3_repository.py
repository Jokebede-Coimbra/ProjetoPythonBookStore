from product import Product
from product_image_interface import ProductImageInterface

class ProductS3Repository(ProductImageInterface):
    
    def __init__(self):
        self.products = []
        
    # def append_product(self, product: Product) -> None:
    #   self.products.append(product)
    
    def put_product(self, product: Product) -> None:
       self.products.append(product)
      
       
    def update_product(self, id:str, product: Product) -> None:
        for product in  self.products:
            if product.id == id:
                return product
            
            return None
    
    def delete_product(self, id:str) -> None:
        if id in self.products:
            del self.products[id]
        return False