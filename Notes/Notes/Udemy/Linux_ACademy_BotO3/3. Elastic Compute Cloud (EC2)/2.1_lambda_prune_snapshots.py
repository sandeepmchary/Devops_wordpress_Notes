import json
import boto3

from pprint import pprint
my_own_id=boto3.client('sts').get_caller_identity().get('Account')
snap_id=[]
def lambda_handler():
    account_id=boto3.client('sts').get_caller_identity().get('Account')
    ec2_cli=boto3.client('ec2')
    #print(account_id)
    #print(account_id.get_caller_identity())
    #print(account_id.get_caller_identity().get('Account'))
    regions=[region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]
    for region in regions:
        #print("Region",region)
        '''
        here we can go with resource but resource only gives the id only we need to 
        sort the snapids with StartTime method we have to go with the response only
        and here if we print the response it will give the response from our id only 
        but gives same result for every region 
        '''
        response=ec2_cli.describe_snapshots(OwnerIds=[account_id])
        snapshots=response['Snapshots']
        # Here we are sorting snapshot by date
        snapshots.sort(key=lambda x: x["StartTime"])
        #snapshots=snapshots[:-2]
    pprint(snapshots)
    print(len(snapshots))   
 
    #print(snap_id)    
    #print(response)        
            
                    

        
    
    


lambda_handler()