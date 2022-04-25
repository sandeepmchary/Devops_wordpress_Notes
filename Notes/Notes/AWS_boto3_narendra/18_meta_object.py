'''
Usage of meta Object
Useful to enter into client object from resource
we have each and every operation with client
but only some operations can be done with resource object
Example with list avaiable ec2 regions
print(dir(ec2_re)) using this we get all the info of the resource object
now we are checking for meta
print(dir(ec2_re.meta)) using this we get all the info of the meta object
print(dir(ec2_re.meta.client))using this we get all the info that we can perform with
client object
ec2_re.meta.client we started with resource now we gone to client object
'''
import boto3
ec2_re=boto3.resource('ec2')
#print(dir(ec2_re))
#print(dir(ec2_re.meta))
#print(dir(ec2_re.meta.client))
#print(ec2_re.meta.client.describe_regions()['Regions'])
for each in ec2_re.meta.client.describe_regions()['Regions']:
    print(each['RegionName'])