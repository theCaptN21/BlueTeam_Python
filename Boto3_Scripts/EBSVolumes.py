#Creating an AWS EBS Volume from Snapshots
import boto3

ec2_client=boto3.client("ec2")
ec2_client.create_snapshot( Description='snapshot from cloud9volume using python',
       VolumeId='YourVolumeID')
       

#Creating an AWS EBS Volume from a Snapshot
import boto3

ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1c',
      Encrypted=True,
      Size=10,
      SnapshotId='snap-YourSnapshotID',
      VolumeType='gp2')

#Describing an AWS EBS Snapshot 
import boto3

ec2_boto3=boto3.client("ec2")
ec2_boto3.describe_snapshots(SnapshotIds=[
          'YourSnapshotId',
      ])

#Deleting AWS EBS Volume Snapshots
import boto3

ec2_client=boto3.client("ec2")
ec2_client.delete_snapshot("SnapshotId='YourSnapshotId")




