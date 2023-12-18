import json

from flask import Flask, jsonify
from flask_cors import CORS

from facades.product_facade import ProductFacade
from repositories.product_dynamodb_repository import ProductDynamodbRepository
from repositories.product_s3_repository import ProductS3Repository
from services.product_service import ProductService

product_dynamodb_repository: ProductDynamodbRepository = ProductDynamodbRepository()
product_s3_repository: ProductS3Repository = ProductS3Repository()
product_service: ProductService = ProductService(
    product_dynamodb_repository, product_s3_repository
)
product_facade: ProductFacade = ProductFacade(product_service)


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*", "headers": "*"}})


@app.route('/')
def home():
    return '*****CattleyaBooks*****'


@app.get('/products')
def get():
    products = product_facade.get()

    products_list = [{'id': product.id,
                      'name': product.name,
                      'author': product.author,
                      'rating': product.rating,
                      'file_name': product.file_name,
                      'price': product.price} for product in products]

    json_response = jsonify(products_list)

    return json_response

@app.get('/products/<string:product_id>')
def get_by_id(product_id):
    product = product_facade.get_by_id(product_id)

    json_response = jsonify(product.to_dict())

    return json_response


@app.route("/version")
def version():
    return "v1.0.0.0"


@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
