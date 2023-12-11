from flask import Flask
import logging
import os

import boto3
'''
logger = logging.getLogger()
logger.setLevel(logging.INFO)
region: str = os.environ.get("sa-east-1")
bucket_name: str = os.environ.get("images-books-labs")
table_name: str = os.environ.get("Books")
s3_client = boto3.client('s3')
dynamodb_client = boto3.resource("dynamodb", region_name=region)
table = dynamodb_client.Table(table_name)
'''
dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')
table_name = 'Books'
bucket_name = 'images-books-labs'
table = dynamodb.Table(table_name)

app = Flask(__name__)

@app.route('/')
def home():
    return '*****CattleyaBooks*****'

@app.route('/products', methods=['GET'])
def get():
    
    data = table.scan()
    response = data["Items"]
    return response

@app.route("/")
def version():
    return "v1.0.0.0"

@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
