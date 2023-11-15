from Facade.facade import Facade

class ConsoleProduct:
   
    def __init__(self, facade: Facade) -> None:
        self.facade = facade
        
    def get_input_product(self) -> None:
        
        name = input("Digite o nome do livro: ") 
        title = input("Digite o título do livro: ") 
        author = input("Digite o autor do livro: ") 
        rating = input("Digite o classificação do livro: ")
        price = input("Digite o preco do livro: ")
        
        prod = (f'Nome: {name}, 
                Título: {title}, 
                Autor: {author}, 
                Classificação: {rating}, 
                Price: {price}')
        
        result = self.facade.product_create(prod)
        
        print(result)
        
        return result
