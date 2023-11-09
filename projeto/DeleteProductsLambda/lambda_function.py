import base64
import json
import logging
import os
import uuid

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
region: str = os.environ.get("AWS_REGION")
bucket_name: str = os.environ.get("bucketName")
table_name: str = os.environ.get("tableName")
s3_client = boto3.client('s3')
dynamodb_client = boto3.resource("dynamodb", region_name=region)
table = dynamodb_client.Table(table_name)


def handler(event, context):

    body = json.loads(event['body'])
    product_id = body["Id"]  

    response = table.get_item(Key={"Id": product_id})
    if "Item" not in response:
        return {
            'statusCode': 404,
            'body': json.dumps("Produto não encontrado.")
        }

    table.delete_item(Key={"Id": product_id})

    return {
        'statusCode': 200,
        'body': json.dumps(f"Produto excluído com sucesso!")
    }
           