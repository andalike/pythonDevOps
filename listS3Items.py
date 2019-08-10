import boto3
s3_resource = boto3.resource('s3')
from boto.s3.connection import S3Connection

conn = S3Connection()
bucket = conn.get_bucket('ankit20292029')
for obj in bucket.get_all_keys():
    print(obj.key)