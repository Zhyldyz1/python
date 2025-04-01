import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0c02fb55956c7d316',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-name',
    SecurityGroups=['your-sg'],
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': 'DevOps-EC2'}]
    }]
)

print("Launched EC2 Instance ID:", instance[0].id)