import boto3

from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('MyFavoriteBooks')

print("Who is the Author of Container Security?")

response = table.query(
    KeyConditionExpression=Key('Author').eq('Liz Rice')
)

for i in response['Items']:
        print(i['Author'], ":", i['BookTitle'])
        
        