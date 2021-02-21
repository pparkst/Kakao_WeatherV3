from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key
from decimal import Decimal

def get_userSet(key, value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('tbl_weatheruserset')

    try:
        #response = table.get_item(Key={key: value})
        #response = table.query (KeyConditionExpression=Key('key').eq(key) & Key('dt').between('2018-07-02', '2018-07-03'))
        response  = table.query (KeyConditionExpression=Key(key).eq(value))
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']


if __name__ == '__main__':
    userSet = get_userSet('id', '1a2a3a',)
    if userSet:
        print("Get userSet succeeded:")
        pprint(userSet, sort_dicts=False)