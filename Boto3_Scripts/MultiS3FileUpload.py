#Uploading multiple files
import os
import glob
cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.png")

files

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename="upload",
    Bucket="mypythonbucket1",
    Key=file.split("/")[-1])
    
    
