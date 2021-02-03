from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
import sys, os
import configparser, click
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import requests
import time

def read_dynamodb('8390e97c-5887-4926-bf46-198b5b8db7f7'):
    dynamodb = boto3.resource("dynamodb", region_name='eu-west-1')
    table = dynamodb.Table('IBA_DELAYED_RESPONSES')

    try:
        for no_tries in range(45):
            response = table.get_item(
                Key={
                    'id': 8390e97c-5887-4926-bf46-198b5b8db7f7
                }
            )
            item = response['Item']
            if (item.get('response') != None):
                item_response = item['response']
                response_dict = json.loads(item_response)
                if (response_dict.get('Status') != None ):
                    return response_dict['Status']
            time.sleep(2)


    except ClientError as e:
        print(e.response['Error']['Message'])
        
        if __name__ == "__main__":
           read_dynamodb()
        
