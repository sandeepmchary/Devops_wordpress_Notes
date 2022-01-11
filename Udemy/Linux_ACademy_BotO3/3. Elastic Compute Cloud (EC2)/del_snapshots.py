import boto3
def lambda_handler():
	account_id=boto3.client('sts').get_caller_identity().get('Account')
	ec2_cli=boto3.client('ec2')
	regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
	for region in regions:
		print("Region: ",region)
		ec2_cli=boto3.client('ec2',region_name=region)
		response=ec2_cli.describe_snapshots(OwnerIds=[account_id])
		#print(response)
		snapshots=response['Snapshots']
		snapshots.sort(key=lambda x: x['StartTime'])
		snapshots=snapshots[:-1]
		
		
		for snapshot in snapshots:
			#print(snapshot)
			id=snapshot['SnapshotId']
			#print("The snapshot id: {} from the region: {}".format(id,region))
			try:
				print("Deleting snapshot id",id)
				ec2_cli.delete_snapshot(SnapshotId=id)
			except:
				if 'InvalidSnapshot.Inuse' in e.message:
					print("Snapshot {} in use, skipping".format(id))
					continue

				


			

lambda_handler()	