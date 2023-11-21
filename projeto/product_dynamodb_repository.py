from product import Product
from product_repository_interface import ProductRepositoryInterface

class ProductDinamodbRepository(ProductRepositoryInterface):
    
    def __init__(self) -> None:
       self.products: list[Product] = []
      
    def append_product(self, product: Product) -> None:
       self.products.append(product)
       
    def update_product(self, id:str, product: Product) -> None:
       for product in  self.products:
            if product.id == id:
                return product
            
            return None
     
    # if id in [product.id for product in self.products]:
        
    def delete_product(self, id:str) -> None:
        if id in self.products:
            del self.products[id]
        return False