import boto3
client=boto3.client('ec2')
response=client.describe_tags()
for reservation in response['Tags']:
	print(reservation['Value'])
	'''
	print("The instance id is" ,reservation['ResourceId'])
	print("The ResourceType is: ", reservation['ResourceType'])
	print("The value is :",reservation['Value'])
	
	print(reservation['ResourceType'])
	print(reservation['Value'])
	'''
	'''
    for instance in reservation['Instances']:
        print("Instanceid for {} ".format(instance['InstanceId']))
    '''