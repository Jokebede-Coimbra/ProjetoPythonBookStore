from io import BytesIO
from pathlib import Path

from interfaces.product_image_interface import ProductImageInterface


class ProductLocalImageRepository(ProductImageInterface):

    def put(self, file_name: str, image: BytesIO) -> None:
        with open(file_name, "wb") as file:
            file.write(image)

    def replace(self, file_name: str, image: BytesIO) -> None:

        if Path(file_name).exists():
            Path(file_name).unlink()
            self.put(file_name, image)

    def remove(self, file_name: str) -> None:

        if Path(file_name).exists():
            Path(file_name).unlink()
