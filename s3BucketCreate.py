import boto3
s3_resource = boto3.resource('s3')

s3_resource.create_bucket(Bucket="ankit202920291",
                          CreateBucketConfiguration={
                              'LocationConstraint': 'eu-west-1'})