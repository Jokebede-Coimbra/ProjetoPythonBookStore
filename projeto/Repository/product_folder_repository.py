from product import Product
from product_repository_interface import ProductRepositoryInterface

class ProductFolderRepository(ProductRepositoryInterface):
    
    def __init__(self) -> None:
      self.products: list[Product] = []
      
    def append_product(self, product: Product) -> None:
       self.products.append(product)
       
    def update_product(self, id:str, product: Product) -> None:
        if id in self.products:
            self.products[id] = product
            return True
        return False
    
    def delete_product(self, id:str) -> None:
        if id in self.products:
            del self.products[id]
        return False