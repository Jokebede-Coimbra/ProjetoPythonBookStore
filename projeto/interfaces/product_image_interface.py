from abc import ABC, abstractmethod
from io import BytesIO


class ProductImageInterface(ABC):

    @abstractmethod
    def put_product_file(self, file_name: str, image: BytesIO) -> None:
        pass

    @abstractmethod
    def replace_product_file(self, file_name, image) -> None:
        pass

    @abstractmethod
    def remove_product_file(self, file_name, image) -> None:
        pass

    @abstractmethod
    def store_image_from_path(self, source_path: str, destination_path: str) -> None:
        pass

    @abstractmethod
    def get_image_stream(self, image_path: str) -> bytes:
        pass
