import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('MyFavoriteBooks')
response = table.scan()
data = response['Items']

for item in data:
    print(item)

