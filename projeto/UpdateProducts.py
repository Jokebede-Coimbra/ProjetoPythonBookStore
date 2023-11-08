import base64
import json
import logging
import os
import boto3
import uuid
import json
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)
region: str = os.environ.get("AWS_REGION")
bucket_name: str = os.environ.get("bucketName")
table_name: str = os.environ.get("tableName")
s3_client = boto3.client('s3')
dynamodb_client = boto3.resource("dynamodb", region_name=region)
table = dynamodb_client.Table(table_name)




def handler(event, context):
    print("Event json %s" % json.dumps(event))
    print("Context %s" % context)

    client = boto3.resource('dynamodb')
    table = client.Table('Books')
  
    rating = Decimal(str(event['rating']))
    price = Decimal(str(event['price']))

    response = table.put_item(
        Item={
            'Id': event['Id'],
            'name': event['name'],
            'rating': rating,
            'author': event['author'],
            'price': price
        }
    )


    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': json.dumps(f"Produto atualizado com sucesso!")
    }
