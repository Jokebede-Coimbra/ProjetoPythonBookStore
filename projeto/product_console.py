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


product_dynamodb_repository: ProductDynamodbRepository = ProductDynamodbRepository()
product_s3_repository: ProductS3Repository = ProductS3Repository()
product_service: ProductService = ProductService(
    product_dynamodb_repository, product_s3_repository)
product_facade: ProductFacade = ProductFacade(product_service)


def display_menu():
    print("========================")
    print("*****CattleyaBooks*****")
    print("1. Adicionar Livro")
    print("2. Atualizar Livro")
    print("3. Remover Livro")
    print("4. Sair")
    print("========================")
    

def get_input_product():
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


while True:
    display_menu()
    opcao = input("Escolha uma opção: ")
    match opcao: 
        case "1":
            product, image = get_input_product()
            result = product_facade.create(product, image)
            print(result)

        case "2":
            id = input("Digite o ID do livro que deseja atualizar: ")
            product, updated_image = get_input_product()
            updated_product = product_facade.update(id, product, updated_image)
        
            if updated_product:
                print("Livro atualizado com sucesso!")
            else:
                print("Erro ao atualizar o livro.")

        case "3":
            id = input("Digite o ID do livro que deseja remover: ")
            deleted_product = product_facade.delete(id)
        
            if deleted_product:
                print("Livro removido com sucesso!")
            else:
                print("Erro ao remover o livro.")

        case "4":
            print("CattleyaBooks agradece! Até a próxima")
            break
        case _:
            print("Opção inválida. Tente novamente.")