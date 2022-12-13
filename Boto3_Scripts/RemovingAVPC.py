#!/usr/bin/env python3

import boto3

client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId='vpc-yourvpcid'
)
response

