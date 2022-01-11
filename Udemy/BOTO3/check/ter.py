import boto3
from pprint import pprint
ec2_cli=boto3.client('ec2')
keypair=[]
for each in ec2_cli.describe_key_pairs()['KeyPairs']:
	#keypair.append(each['KeyName'])
	print(each['KeyName'])
'''	
print("Before the removing the samdevops",keypair)
# FROM THE APPENDED LIST WE ARE REMOVING THE SAMDEVOPS ONLY NOW THE LIST DOES NOT CONTAIN SAMDEVOPS
keypair.remove('samdevops')
print("After removing samdevops",keypair)
for each_key in keypair:
	response=ec2_cli.delete_key_pair(KeyName=each_key)
print(response)	
	    			
#pprint(ec2_cli.delete_key_pair(KeyName=keypair))

#pprint(ec2_cli.terminate_instances(InstanceIds=['i-05c1e75b7c538ea2f']))
'''