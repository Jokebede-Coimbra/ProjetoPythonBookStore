from interfaces.product_image_interface import ProductImageInterface


class ProductS3Repository(ProductImageInterface):

    def __init__(self):
        pass

    def put_product_file(self, file_name, image) -> None:
        pass

    def replace_product_file(self, file_name, image) -> None:
        pass

    def remove_product_file(self, file_name, image) -> None:
        pass

    def store_image_from_path(self, source_path: str, destination_path: str) -> None:
        pass

    def get_image_stream(self, image_path: str) -> bytes:
        pass
