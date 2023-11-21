from product import Product
# from product_folder_interface import ProductFolderInterface
from product_image_interface import ProductImageInterface
from product_repository_interface import ProductRepositoryInterface

class ProductFolderRepository(ProductRepositoryInterface):
    
    def __init__(self) -> None:
      self.products: list[Product] = []
      
    def append_product(self, product: Product) -> None:
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