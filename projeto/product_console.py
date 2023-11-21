import os
import uuid
from io import BytesIO

from entities.product import Product
from facades.product_facade import ProductFacade
from repositories.product_local_image_repository import \
    ProductLocalImageRepository
from repositories.product_memory_repository import ProductMemoryRepository
from services.product_service import ProductService

product_memory_repository: ProductMemoryRepository = ProductMemoryRepository()
product_local_image_repository: ProductLocalImageRepository = ProductLocalImageRepository()
product_service: ProductService = ProductService(
    product_memory_repository, product_local_image_repository)
product_facade: ProductFacade = ProductFacade(product_service)

id = uuid.uuid4().hex
# name = input("Digite o nome do livro: ")
# author = input("Digite o autor do livro: ")
# rating = int(input("Digite o classificação do livro: "))
# price = float(input("Digite o preço do livro: "))
# image = input("Digite o caminho da imagem do livro: ")
name = "name field"
author = "author field"
rating = 3
price = 10.22
location_image = "D:\Clean Code.jpg"

with open(location_image, 'rb') as f:
    image: BytesIO = f.read()
    extension = os.path.splitext(f.name)[1]
    file_name = f"{id}{extension}"
    
    product = Product(id=id,
                      name=name,
                      author=author,
                      rating=rating,
                      price=price,
                      file_name=file_name)

    result = product_facade.create(product, image)
    print(result)
