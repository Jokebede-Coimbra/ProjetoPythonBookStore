import os
from io import BytesIO

import boto3

from interfaces.product_image_interface import ProductImageInterface


class ProductS3Repository(ProductImageInterface):
    BUCKET_NAME = os.environ.get("bucketName")

    def __init__(self, aws_region='sa-east-1'):
        self.aws_region = aws_region
        self.s3_client = boto3.client('s3', region_name=self.aws_region)

    def put(self, file_name: str, image: BytesIO) -> None:
        self.s3_client.put_object(
            Bucket=ProductS3Repository.BUCKET_NAME,
            Key=file_name,
            Body=image
        )

    def replace(self, file_name: str, new_image: BytesIO) -> None:
        self.put(file_name, new_image)

    def remove(self, file_name: str) -> None:
        self.s3_client.delete_object(
            Bucket=ProductS3Repository.BUCKET_NAME,
            Key=file_name
        )
