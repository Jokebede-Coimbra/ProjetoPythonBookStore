import boto3
from io import BytesIO

from interfaces.product_image_interface import ProductImageInterface

class ProductS3Repository(ProductImageInterface):
    
    def __init__(self, bucket_name='images-books-labs', aws_region='sa-east-1'):
        self.bucket_name = bucket_name
        self.aws_region = aws_region
        self.s3_client = boto3.client('s3', region_name=self.aws_region)

    def put(self, file_name: str, image: BytesIO) -> None:
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=file_name,
            Body=image
        )

    def replace(self, file_name: str, new_image: BytesIO) -> None:
        self.put(file_name, new_image)

    def remove(self, file_name: str) -> None:
        self.s3_client.delete_object(
            Bucket=self.bucket_name,
            Key=file_name
        )
