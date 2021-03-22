import os
import json
from base64 import b64decode

import boto3
from botocore.exceptions import ClientError

from SESClient import SESClient

def lambda_handler(event, context):
    # print("this is the event: " + json.dumps(event))
    # print("this is the encoded event body: " + event["body"])
    event_body = json.loads(b64decode(event["body"]))
    
    RECIPIENT = os.environ["RECIPIENT_EMAIL"]

    BODY_TEXT = event_body["body"]    

    CHARSET = "UTF-8"

    client = SESClient()

    try:
        response = client.send_the_email(RECIPIENT, CHARSET, BODY_TEXT, event_body["email_address"], event_body["subject"])
        if(response["MessageId"]):
            print("Email sent!")
            return {
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    'Access-Control-Allow-Methods': '*'
                },
                "statusCode": 200,
                "body": {
                    "messageId": response["MessageId"]
                },
            }
    # generic exception, though it might just be a KeyError
    except Exception as e:
        print(e)
        {
            "headers": {
                "Access-Control-Allow-Origin": "*",
                'Access-Control-Allow-Methods': '*'
            },
            "statusCode": 500,
            "body": e,
        }
