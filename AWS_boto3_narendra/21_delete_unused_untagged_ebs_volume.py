import boto3
ec2_re=boto3.resource('ec2')
ec2_cli=boto3.client('ec2')
'''
for each_vol in ec2_re.volumes.all():
	print(each_vol.id,each_vol.state)
'''
for each_vol in ec2_re.volumes.filter(
										Filters=[
										{
											"Name":"status",
											"Values":['available']
										}]):
    # we need to identify which are having available and which are untagged
    # if each_vol.tags 'if tags are there it will become true if there are no tabs this will become fail
    if not each_vol.tags:
        print(each_vol.id,each_vol.state,each_vol.tags)
		# Now our next step is delete that
		# go for ec2 AND THEN SELECT VOLUME
        print("Deleting unused and untagged volumes...")
        resp=each_vol.delete()
        print(resp)

 
 