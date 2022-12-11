#!/usr/bin/env python3

#This is a test script to create an AWS S3 Bucket
import boto3

AWS_REGION = "us-west-1"

resource = boto3.resource("s3", region_name=AWS_REGION)

bucket_name = "mypythonbucket1"
location = {'LocationConstraint': AWS_REGION}

bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")


