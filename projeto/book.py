class Book: 
    def __init__(self, id:str, name:str, title:str, author:str, rating:str, price:float) -> None: 
        self.id = id
        self.name = name
        self.title = title
        self.author = author
        self.rating = rating
        self.price = price