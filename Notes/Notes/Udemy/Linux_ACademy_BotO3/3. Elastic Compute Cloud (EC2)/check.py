from datetime import datetime
import boto3
from pprint import pprint
def lambda_handler():
    ec2_cli=boto3.client('ec2')
    regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
    for region in regions:
        ec2_re=boto3.resource('ec2',region_name=region)
        instances=ec2_re.instances.filter(Filters=[{'Name':'tag:backup','Values':['true']}])
        timestamp=datetime.utcnow().replace(microsecond=0).isoformat()
        for i in instances.all():
            print("instances id: ",i)
            print("Only Instance id: ",i.id)
            for v in i.volumes.all():
                print("The volume id: ",v)
                print("The Volume id only: ", v.id)
                 desc='Backup of {0},Value {1},created {2}'.format(i.id,v.id,timestamp)
                snapshot=v.create_snapshot(desc)
                print("Created Snapshot: ",snapshot.id)
                
                
        

lambda_handler()