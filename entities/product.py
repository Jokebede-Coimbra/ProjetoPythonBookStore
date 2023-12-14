import os


class Product:
    def __init__(self, id: str, name: str, author: str, rating: int, price: float, file_name: str) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.price = price
        self.file_name = file_name

    def get_address(self) -> str:
        return f"https://{os.environ.get('bucketName')}.s3.sa-east-1.amazonaws.com/{self.file_name}"

    def to_dict(self) -> dict:
        return {
            'Id': self.id,
            'name': self.name,
            'author': self.author,
            'rating': self.rating,
            'price': self.price,
            'file_name': self.file_name
        }