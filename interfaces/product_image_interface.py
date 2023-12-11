from abc import ABC, abstractmethod
from io import BytesIO


class ProductImageInterface(ABC):

    @abstractmethod
    def put(self, file_name: str, image: BytesIO) -> None:
        pass

    @abstractmethod
    def replace(self, file_name: str) -> None:
        pass

    @abstractmethod
    def remove(self, file_name: str) -> None:
        pass
