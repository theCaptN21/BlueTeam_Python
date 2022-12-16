#Creating Multile EC2 Instances
import boto3

ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='YourAMIId',
      InstanceType='t2.micro',
    MaxCount=3,
      MinCount=3)
      

#Getting Your Instance IDs
import boto3

ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"][0]
data_instance=data["Instances"]
for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")


#Terminating Multiple EC2 Instances
import boto3

ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"]

li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
        
ec2_client.terminate_instances(InstanceIds=li)
    