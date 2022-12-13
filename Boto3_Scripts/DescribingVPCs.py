#!/usr/bin/env python3

import boto3

client=boto3.client("ec2")

#How to describe VPCs in your account
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcID"])
    
#How to describe a single VPC using the VPC ID
x=client.describe_vpcs(VpcIds="vpc-ID")


