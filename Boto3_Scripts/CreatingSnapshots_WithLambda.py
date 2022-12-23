#This is a script to backup on your EC2 Instances, by creating snapshots
from datetime import datetime
import boto3

def lambda_handler(event, context):
    
    #Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]
               
    #Iterate over each region
    for region in regions:
        print('Instances in EC2 Region {0}:'.format(region))
        ec2 = boto3.resources('ec2', region_name=region)
        
        
        #Get only instances with backup tag
        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup', 'Values': ['true']}
            ]
        )
        
        #ISO 8601 timestamp, i.e., 2022-12-23T14:01:55
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
        
        for i in instances.all():
            for v in i.volumes.all():
                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)
                    
                snapshot = v.create_snapshot(Description=desc)
                    
                print("Created snapshot:", snapshot.id)
                    