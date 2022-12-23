from __future__ import print_function
from random import randint
from datetime import datetime
import json
import boto3

print('Function is loading')

#Use this script if you'd like to create a random generator message for SQS
def lambda_handler(event, context):
    
    myNumber = randint(0,100)
    print("Random No. [ %s ]" % myNumber)
    return myNumber
    
    sqs = boto3.client("sqs")
    response = sqs.send_message(
        QueueUrl = 'YourQueueURL', 
        MessageBody = random_number
    )

#Use this script if you'd like to create an SQS message for the date and time    
def lambda_handler(event, context):
    
    sqs = boto3.client("sqs")
    
    current_time = datetime.now()
    timestamp = (f"Here is the current time: {current_time}")
    
    response = sqs.send_message(
        QueueUrl = 'YourQueueURL', 
        MessageBody = timestamp
    )
  
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
  
   
    
    


