import boto3


ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
print("This is coming from REGIONS")
print('Regions:', response['Regions'])

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
print ("This is comming from AVAIL_ZONES")
print('Availability Zones:', response['AvailabilityZones'])