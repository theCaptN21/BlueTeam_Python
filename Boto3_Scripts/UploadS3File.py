#!/usr/bin/env python3
import boto3

#Uploading a single file to S3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="testfile.png",
    Bucket="mypythonbucket1",
    Key="uploadtest.png")


