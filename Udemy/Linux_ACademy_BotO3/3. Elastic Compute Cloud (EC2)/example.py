'''
 we can use life cycle mange but we have to wait over an hour after creation of this policy  and basically it depends on the tags,
 if any over tags are part of the lifecycle then we cannot reuse same tags for another policy if we remove the policy or change the tags of policy all the ebs snapshots we taken previously wont be deleted it billup
 - also copy of this snapshot taken by this policy it wont come under automated deletion we have to remove those manually as-well
 - we can only create snapshots only 12 or 24 hours
 '''
from datetime import datetime
import boto3
def lambda_handler():
    ec2_cli=boto3.client('ec2',region_name='us-east-2')
    regions=[region['RegionName']for region in ec2_cli.describe_regions()['Regions']]
    for region in regions:
        print('Instances in Ec2 Region: {0}'.format(region))
        ec2_re=boto3.resource('ec2',region_name=region)
        instances=ec2_re.instances.filter(
            Filters=[
                {'Name':'tag:backup','Values':['true']}
            ]
        )
        #print(instances)
        
        timestamp=datetime.utcnow().replace(microsecond=0).isoformat()
        for i in instances.all():
            print(i)
            print(i.id)
            for v in i.volumes.all():
                print(v)
                desc='Backup of {0},Value {1},created {2}'.format(i.id,v.id,timestamp)
                print(desc)
                snapshot=v.create_snapshot(Description=desc)
                print("Created Snapshot: ",snapshot.id)
                

lambda_handler()