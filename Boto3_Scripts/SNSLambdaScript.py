import json
import boto3
client = boto3.client("sns")

snsarn = ('YourSNSNARN') 


def lambda_handler(event, context):
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))

    response = client.publish(
                      TopicArn = snsarn,
                      Message = payload)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
