#This is the syntax to create your DynamoDB table:
import boto3


#This is how we will interact with the AWS service
new_dynamodb = boto3.resource('dynamodb')

#This is the syntax to create the table
table = new_dynamodb.create_table (
    AttributeDefinitions = [
        {
            'AttributeName': 'Author',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'BookTitle',
            'AttributeType': 'S'
        }
    ],
    TableName='MyFavoriteBooks',
    KeySchema=[
        {
             'AttributeName': 'Author',
             'KeyType': 'HASH'
        },
        {
             'AttributeName':'BookTitle',
             'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
          
)

print(table)


