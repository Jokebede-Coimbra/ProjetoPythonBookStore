import base64
import json
import logging
import os
import uuid
import boto3

import json
from decimal import Decimal
from facades.product_facade import ProductFacade
from entities.product import Product
from services.product_service import ProductService
from repositories.product_dynamodb_repository import ProductDynamodbRepository
from repositories.product_s3_repository import ProductS3Repository

product_dynamodb_repository: ProductDynamodbRepository = ProductDynamodbRepository()
product_s3_repository: ProductS3Repository = ProductS3Repository()
product_service: ProductService = ProductService(
    product_dynamodb_repository, product_s3_repository
)
product_facade: ProductFacade = ProductFacade(product_service)


def insert_handler(event, context):
    body = json.loads(event["body"])

    # file_name = body["fileName"]
    product_id = str(uuid.uuid4())
    product_dict = {
        "Id": product_id,
        "Name": body["name"],
        "Rating": str(body["rating"]),
        "Author": body["author"],
        "Price": str(body["price"]),
        "FileName": product_id,
    }

    base64_image = body.get("filebase64")
    if base64_image:
        image = base64.b64decode(base64_image)

    product = Product(
        product_id,
        product_dict.get("Name"),
        product_dict.get("Author"),
        product_dict.get("Rating"),
        product_dict.get("Price"),
        product_dict.get("FileName"),
    )

    product_facade.create(product, image)

    response = {
        "statusCode": 200,
        "body": json.dumps(f"Product inserted successfully {product}!"),
    }

    return response


def update_handler(event, context):
    body = json.loads(event["body"])

    id = body.get("Id")
    file_name = body.get("file_name")
    product_dict = {
        "Id": id,
        "Name": body.get("name"),
        "Rating": str(body.get("rating")),
        "Author": body.get("author"),
        "Price": str(body.get("price")),
        "FileName": file_name,
    }

    base64_image = body.get("filebase64")
    if base64_image:
        image = base64.b64decode(base64_image)

    product = Product(
        id,
        product_dict.get("Name"),
        product_dict.get("Author"),
        product_dict.get("Rating"),
        product_dict.get("Price"),
        product_dict.get("FileName"),
    )

    product_facade.update(id, product, image)

    response = {
        "statusCode": 200,
        "body": json.dumps(f"Product updated successfully {product}!"),
    }

    return response


def get_by_id_handler(event, context):
    product_id = event["pathParameters"]["id"]

    product = product_facade.get_by_id(product_id)

    response = {
        "statusCode": 200,
        "body": json.dumps(f"Product found successfully {product.to_dict()}!"),
    }

    return response


def delete_handler(event, context):
    body = json.loads(event["body"])

    product_id = body["Id"]

    product_facade.delete(product_id)

    response = {
        "statusCode": 200,
        "body": json.dumps(f"Product deleted successfully {product_id}!"),
    }

    return response
