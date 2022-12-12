#!/usr/bin/env python3

#Deleting a single S3 object
import boto3
s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket='mypythonbucket1', Key='uploadtest.png')

#Deleting multiple S3 objects
import os
import glob
#Finding all objects from buckets
objects=s3_resource.list_objects(Bucket="mypythonbucket1")["contents"]
len(objects)
#Iteration
for object in objects:
    response=s3_resource.delete_object(Bucket="mypythonbucket1", 
    Key=object["Key"])
    print(response)
    
    

