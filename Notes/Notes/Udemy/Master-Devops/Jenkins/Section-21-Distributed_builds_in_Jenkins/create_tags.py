import boto3
client = boto3.client('ec2')
response = client.create_tags(
    Resources=['i-0b216f34725c517bc'],
    Tags=[
        {
            'Key':'Name',
            'Value': 'jenkins_slave'
        }
    ]
)