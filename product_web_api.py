from flask import Flask, jsonify
from facades.product_facade import ProductFacade
from services.product_service import ProductService
from repositories.product_dynamodb_repository import ProductDynamodbRepository
from repositories.product_s3_repository import ProductS3Repository

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
    return  jsonify(response)

@app.route("/")
def version():
    return "v1.0.0.0"

@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)