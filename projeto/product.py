class Product:
    def __init__(self, id: str, name: str, author: str, rating: int, price: float, image: str) -> None: 
        self.id = id
        self.name = name
        self.author = author
        self.rating = rating
        self.price = price
        self.image = image
