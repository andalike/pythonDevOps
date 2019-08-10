import boto3
ids = ['i-0b9c1e74bfbd34a1c']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop() #for stopping an ec2 instance