import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyFavoriteBooks')

item_1 = {"Author":"John Culkin & Mike Zazon", "BookTitle":"AWS Cookbook"}
item_2 = {"Author":"Casey Rosental & Nora Jones", "BookTitle":"Chaos Engineering"}
item_3 = {"Author":"Jonathan Allen & Thomas Blood", "BookTitle":"Reaching Cloud Velocity"}
item_4 = {"Author":"Liz Rice", "BookTitle":"Container Security"}
item_5 = {"Author":"Murat Erder, Pierre Pureur, & Eoin Woods", "BookTitle":"Continuous Architecture In Practice"}
item_6 = {"Author":"Merih Taze", "BookTitle":"Engineers' Survival Guide"}
item_7 = {"Author":"Marc Hornbeek", "BookTitle":"Engineering Devops"}
item_8 = {"Author":"Glenn Wilson", "BookTitle":"DevSecOps"}
item_9 = {"Author":"Kim, Humble, Debois, & Willis", "BookTitle":"DevOps Handbook"}
item_10 = {"Author":"Don Clifton", "BookTitle":"Discover Your CliftonStrengths"}

items_to_add = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10]

with table.batch_writer() as batch:
    for item in items_to_add:
        response = batch.put_item(Item={
            "Author": item["Author"],
            "BookTitle": item["BookTitle"]
    }
)

items_to_delete = [item_1, item_2]

with table.batch_writer() as batch:
    for item in items_to_delete:
        response = batch.put_item(Item={
            "Author": item["Author"],
            "BookTitle": item["BookTitle"]
    }
)

print("Table Successfully Updated")

