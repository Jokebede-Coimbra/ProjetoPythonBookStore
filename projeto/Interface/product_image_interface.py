from abc import ABC, abstractmethod

class ProductImageInterface(ABC):
    
    @abstractmethod
    def put_product_file(self, file_name, image) -> None:
        pass
    @abstractmethod
    def replace_product_file(self, file_name, image) -> None:
        pass
    @abstractmethod
    def remove_product_file(self, file_name, image) -> None:
        pass
