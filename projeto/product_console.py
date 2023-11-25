from decimal import Decimal
import os
import uuid
from io import BytesIO

from entities.product import Product
from facades.product_facade import ProductFacade
from repositories.product_dynamodb_repository import ProductDynamodbRepository
from repositories.product_local_image_repository import \
    ProductLocalImageRepository
from repositories.product_memory_repository import ProductMemoryRepository
from repositories.product_s3_repository import ProductS3Repository

from services.product_service import ProductService

'''
product_memory_repository: ProductMemoryRepository = ProductMemoryRepository()
product_ss3_repository: ProductSS3Repository = ProductSS3Repository()
product_service: ProductService = ProductService(
    product_memory_repository, product_ss3_repository)
product_facade: ProductFacade = ProductFacade(product_service)
'''

# name = input("Digite o nome do livro: ")
# author = input("Digite o autor do livro: ")
# rating = int(input("Digite o classificação do livro: "))
# price = float(input("Digite o preço do livro: "))
# image = input("Digite o caminho da imagem do livro: ")
id = uuid.uuid4().hex
name = "name field"
author = "author field"
rating = 3
price = Decimal("10.99")
location_image = "D:\Clean+Architecture.jpg"

with open(location_image, 'rb') as f:
    image: BytesIO = f.read()
    # image = BytesIO(f.read()) s3 
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