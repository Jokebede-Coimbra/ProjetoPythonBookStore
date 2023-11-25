from decimal import Decimal
import uuid
from io import BytesIO

from entities.product import Product
from facades.product_facade import ProductFacade
from product_user_interface_console import UserInterface
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

product_facade = ProductFacade(product_service)
user_interface = UserInterface(product_facade)

id = uuid.uuid4().hex

def display_product():
    print("========================")
    print("*****CattleyaBooks*****")
    print("1. Adicionar Livro")
    print("2. Atualizar Livro")
    print("3. Remover Livro")
    print("4. Sair")
    print("========================")
    
    

while True:
    display_product()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        product, image = user_interface.get_product()
        result = user_interface.product_facade.create(product, image)
        print(result)

    elif opcao == "2":
        id = input("Digite o ID do livro que deseja atualizar: ")
        product, updated_image =  user_interface.get_product()
        updated_product =  user_interface.product_facade.update(id, product, updated_image)
        
        if updated_product:
            print("Livro atualizado com sucesso!")
        else:
            print("Erro ao atualizar o livro.")

    elif opcao == "3":
        id = input("Digite o ID do livro que deseja remover: ")
        deleted_product = user_interface.product_facade.delete(id)
                
        if deleted_product:
            print("Livro removido com sucesso!")
        else:
            print("Erro ao remover o livro.")

    elif opcao == "4":
            print("CattleyaBooks agradece. Até logo!")
            break
    else:
            print("Opção inválida. Tente novamente.")


