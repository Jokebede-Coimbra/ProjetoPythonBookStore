import boto3
from decimal import Decimal
from interfaces.product_repository_interface import ProductRepositoryInterface
from entities.product import Product

class ProductDynamodbRepository(ProductRepositoryInterface):
    
    def __init__(self, table_name='Books', region_name="sa-east-1") -> None:
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.table_name = table_name
        self.table = self.dynamodb.Table(self.table_name)

    def append(self, custom_table: Product) -> None:
        response = self.table.put_item(Item=custom_table.to_dict())
        return response

    def update(self, id: str, updated_product: Product) -> Product:
        update_expression = "SET #name = :name, #author = :author, #rating = :rating, #price = :price, #file_name = :file_name"
        expression_attribute_values = {
            ':name': updated_product.name,
            ':author': updated_product.author,
            ':rating': updated_product.rating,
            ':price': updated_product.price,
            ':file_name': updated_product.file_name
        }
        expression_attribute_names = {
            '#name': 'name',
            '#author': 'author',
            '#rating': 'rating',
            '#price': 'price',
            '#file_name': 'file_name'
        }

        response = self.table.update_item(
            Key={"Id": id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names,
            ReturnValues="ALL_NEW"
        )

        updated_attributes = response.get('Attributes', {})

        return Product(
            updated_attributes['Id'],
            updated_attributes['name'],
            updated_attributes['author'],
            updated_attributes['rating'],
            updated_attributes['price'],
            updated_attributes['file_name']
    )
    
    def get(self, id: str) -> Product:
        response = self.table.get_item(Key={'Id': id})
        item = response.get('Item')

        if item:
            return Product(
                item['Id'],
                item.get('name'),
                item.get('author'),
                item.get('rating'),
                item.get('price'),
                item.get('file_name')
            )
        return None
            
    def delete(self, id: str) -> None:
        response = self.table.delete_item(Key={'Id': id})
        return response
