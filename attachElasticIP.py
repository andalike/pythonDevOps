import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    allocation = ec2.allocate_address(Domain='vpc')
    response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                     InstanceId='i-0c70c46e2a6cf24eb')
    print(response)
except ClientError as e:
    print(e)