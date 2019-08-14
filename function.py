import boto3
ec2 = boto3.resource('ec2')
s3_resource = boto3.resource('s3')

def createInstence():
    print("Inside Create Instance Function")
    instance = ec2.create_instances(
    ImageId = 'ami-07d0cf3af28718ef8',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = '27june',
    SubnetId = 'subnet-e58503cb')
    print ("Instance Created with Instance Id->",instance[0].id)
    createBucket()

def createBucket():
    print("Inside Create Bucket Function")
    s3_resource.create_bucket(Bucket="bucket20192010")
    print("Bucket Successfully Created")


createInstence()
