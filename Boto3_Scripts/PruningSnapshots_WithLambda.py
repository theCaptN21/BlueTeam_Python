#This is a script to prune your snapshots using Lambda
import boto3

def lambda_handler(event, context):
    
    #Get list of regions and accout information
    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]
               
    for region in regions:
        print("Region:", region)
        ec2 = boto3.resources('ec2', region_name=region)
        
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response["Snapshots"]
        
        #Sort snapshots by date ascending
        snapshots.sort(key=lambda x: x["StartTime"])
        
        #Remove snapshots we want to keep (3 most recent)
        snapshots = snapshots[:-3]
        
        for snapshot in snapshots:
            id = snapshot['SnapshotId']
            try:
                print("Deleting snapshot:", id)
                ec2.delete_snapshot(SnapshotId=id)
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print("Snapshot {} in use, skipping.".format(id))
                    continue
    
        
