class Product:
    def __init__(self, id: str, name: str, author: str, rating: int, price: float, file_name: str) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.price = price
        self.file_name = file_name
