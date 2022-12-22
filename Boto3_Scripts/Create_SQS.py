#This is a simple script to create an SQS Queue
import boto3

def create_queue():
    sqs_client = boto3.client('sqs')
    response = sqs_client.create_queue(
        QueueName="wk-15-queue",
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    
print(queue.url)




    
