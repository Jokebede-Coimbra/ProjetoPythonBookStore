from decimal import Decimal

class Product:
    def __init__(self, id: str, name: str, author: str, rating: int, price: Decimal, file_name: str) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.price = price
        self.file_name = file_name

    def to_dict(self) -> dict:
        return {
            'Id': self.id,
            'name': self.name,
            'author': self.author,
            'rating': self.rating,
            'price': self.price,
            'file_name': self.file_name
        }