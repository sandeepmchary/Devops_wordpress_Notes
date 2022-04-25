import boto3
aws_mgm_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mgm_con.resource(service_name="ec2",region_name="us-east-2")
# VALUES ARE ALWAYS LIST SO WE USE []
f_ebs_unused={"Name":"status","Values":["available"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[f_ebs_unused]):
	#  IN THE BOTO3 DOCUMENTATION FOR EC2 TABLE OF CONTENT WE HAVE ONE SET FOR VOLUMES
	#  FROM THERE WE GOT THESE ID AND STATE
	if not each_volume.tags:
		print(each_volume.id,each_volume.state,each_volume.tags)
		print("Deleting untagged and available volumes ......")
		each_volume.delete()
print("Deleted volumes")		