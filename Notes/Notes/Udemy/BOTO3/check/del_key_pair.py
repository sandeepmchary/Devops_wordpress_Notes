import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
key_pairs=[]
for each in ec2_cli.describe_key_pairs()['KeyPairs']:
	key_pairs.append(each['KeyName'])
print(key_pairs)	
key_pairs.remove('samdevops')
for each_key in key_pairs:
	response=ec2_cli.delete_key_pair(KeyName=each_key)
print(response)	