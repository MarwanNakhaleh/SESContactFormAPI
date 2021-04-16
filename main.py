import os
import json
from base64 import b64decode, b64encode
import logging

import boto3
from botocore.exceptions import ClientError

from SESClient import SESClient

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)


def lambda_handler(event, context):
    try:
        logging.info(json.dumps(event))
        event_body = json.loads(b64decode(event["body"]))
        RECIPIENT = os.environ["RECIPIENT_EMAIL"]
        BODY_TEXT = event_body["body"]
        CHARSET = "UTF-8"
    
        client = SESClient()
    
        response = client.send_the_email(
            RECIPIENT, CHARSET, BODY_TEXT, event_body["email_address"], event_body["subject"])
        if(response["MessageId"]):
            return {
                "headers": {
                    "Access-Control-Allow-Origin": "'https://branson.solutions', 'https://www.branson.solutions'",
                    'Access-Control-Allow-Methods': '*'
                },
                "statusCode": 200,
                "body": response["MessageId"]
            }
    # generic exception, though it might just be a KeyError
    except Exception as e:
        print("ERROR: " + str(e))
        {
            "headers": {
                "Access-Control-Allow-Origin": "'https://branson.solutions', 'https://www.branson.solutions'",
                'Access-Control-Allow-Methods': 'POST'
            },
            "statusCode": 500,
            "body": str(e)
        }
