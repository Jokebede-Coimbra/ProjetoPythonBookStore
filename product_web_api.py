from flask import Flask, jsonify

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

@app.route('/')
def home():
    return '*****CattleyaBooks*****'

@app.route('/products')
def get():
    response = product_facade.get()
    return  response

@app.route("/version")
def version():
    return "v1.0.0.0"

@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
