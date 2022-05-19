import boto3
ec2_cli=boto3.client('ec2')
response=ec2_cli.describe_tags(
    Filters=[
        {
            'Name': 'resource-type',
            'Values': ['instance']
        },
    ],
)
for each in response['Tags']:
    print(each['Value'])