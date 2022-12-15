import boto3

#Create your key pair
key_pair=ec2_resource.create_key_pair(KeyName='YourKeyPairName')
key_value=key_pair.key_material

import io
with io.open("YourKeyPairName.pem", "w", encoding="utf-8")as f1:
  f1.write(str(key_value))
  f1.close()

#Create your Security Group
ec2_client=boto3.client("ec2")
ec2_client.create_security_group(Description='DescriptionofyourSG',
      GroupName='YourSG Name')
      
#Enable inbound rules for the Security Group
ec2_client.authorize_security_group_ingress(
      GroupID='YourSGID',
      IpPermissions=[
        {
              'FromPort: 0,
              'IpProtocol' : '-1',
              'IpRanges' : [
                {
                      'CidrIp' : '0.0.0.0/0',
                },
            ],
            'ToPort' : 65536,
        }
    ]
            )

#
        
