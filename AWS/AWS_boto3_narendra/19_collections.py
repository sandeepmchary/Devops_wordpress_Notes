'''
- collectively usage of all ec2 is called collections
- print(ec2_re.instances)
- ec2.instancesCollectionManager(ec2.ServiceResource(), ec2.Instance) this is an object
- here we are concentrating on all,limit,iterator,filter
- here we are using all so we use for loop for this 
- for collection method we mostly use filter
- Filter is argument method for filter
- Filter is list,it contains a dictionary
- each dictionary is like one filter
'''
import boto3
ec2_re=boto3.resource('ec2')
#print(ec2_re.instances)
#print(dir(ec2_re.instances))
#print(ec2_re.instances.all())
f1={'Name':'instance-state-name','Values':['stopped','running']}
f2={'Name':'instance-type','Values':['t2.micro']}
for each in ec2_re.instances.filter(Filters=[f1,f2]):
	print(each)