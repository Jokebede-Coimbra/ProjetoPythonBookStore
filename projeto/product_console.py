from pathlib import Path
from facade import Facade
from product import Product
from product_folder_repository import ProductFolderRepository
from product_local_image_repository import LocalImageRepository
from product_local_repository import ProductLocalRepository
from product_service import ProductService
from PIL import Image


class ProductConsole:
   
    def __init__(self, facade: Facade, image_repository: LocalImageRepository) -> None:
        self.facade = facade
        self.image_repository = image_repository


    def get_input_product(self) -> None:
        id = input("Digite a identificação do livro: ")
        name = input("Digite o nome do livro: ")
        author = input("Digite o autor do livro: ")
        rating = int(input("Digite o classificação do livro: "))  
        price = float(input("Digite o preço do livro: "))
        image = input("Digite o caminho da imagem do livro: ")


        product = Product(id=id, name=name, author=author, rating=rating, price=price, image=image)

        destination_directory = "C:/Users/jkbd_/Desktop/Python/ProjetoFinal/projeto/Image"

        file_name = f"{id}_image.jpg"
        
        self.image_repository.store_image_from_path(image, Path(destination_directory) / file_name)

        result = self.facade.product_create(product)
        print(result)


        img = Image.open(Path(destination_directory) / file_name)
        img.show()


        return result


folder = ProductFolderRepository()
product_image = LocalImageRepository()
product_local = ProductLocalRepository()
product_service = ProductService(product_image, folder)
facade = Facade(product_service)
product_console = ProductConsole(facade, product_image)


product_console.get_input_product()