from decimal import Decimal
import os
import uuid
from io import BytesIO

from facades.product_facade import ProductFacade
from entities.product import Product

class UserInterface:
    
    def __init__(self, product_facade: ProductFacade):
        self.product_facade = product_facade

    def get_product(self):
        id = uuid.uuid4().hex
        name = input("Digite o nome do livro: ")
        author = input("Digite o autor do livro: ")
        rating = int(input("Digite a classificação do livro: "))
        price = Decimal(input("Digite o preço do livro: "))
        image_path = input("Digite o caminho da imagem do livro: ")

        with open(image_path, 'rb') as f:
             # image: BytesIO = f.read()
            image = BytesIO(f.read())
            extension = os.path.splitext(f.name)[1]
            file_name = f"{id}{extension}"

        return Product(id=id, name=name, author=author, rating=rating, price=price, file_name=file_name), image