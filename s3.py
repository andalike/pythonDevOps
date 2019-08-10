import boto3
s3_resource = boto3.resource('s3')
import uuid
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


s3_resource.create_bucket(Bucket="ankit20292029",
                          CreateBucketConfiguration={
                              'LocationConstraint': 'eu-west-1'})