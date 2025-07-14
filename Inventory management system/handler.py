import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('InventoryTable')

def create_item(event, context):
    data = json.loads(event['body'])
    item = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'quantity': data['quantity']
    }
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item created', 'item': item}),
        'headers': {'Access-Control-Allow-Origin': '*'}
    }

def get_item(event, context):
    item_id = event['pathParameters']['id']
    response = table.get_item(Key={'id': item_id})
    item = response.get('Item', {})
    return {
        'statusCode': 200,
        'body': json.dumps(item),
        'headers': {'Access-Control-Allow-Origin': '*'}
    }