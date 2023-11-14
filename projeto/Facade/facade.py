from Services.product_service import ProductService

class Facade:
    
    def __init__(self, product_service: ProductService):
      self.product_service = product_service
      
      
    def product_create(self, product):
        self.product_service.create_product(product)
        
    def product_update(self, id, up_product):
        self.product_service.update_product(id, up_product)
        
    def product_delete(self, id: str):
        self.product_service.delete_product(id)