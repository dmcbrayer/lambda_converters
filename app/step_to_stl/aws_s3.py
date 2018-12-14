import boto3
import os

class AwsS3():
    def __init__(self):
        self.client = boto3.client('s3')

    def get_object(self, bucket, key, destination):
        self.client.download_file(bucket, key, destination)

    def put_object(self, filepath, s3_bucket, s3_key):
        self.client.upload_file(filepath, s3_bucket, s3_key)

    def get_object_url(self, bucket, key):
        self.client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': key}, ExpiresIn = 1000)

