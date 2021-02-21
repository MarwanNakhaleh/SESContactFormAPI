import os
import json
from base64 import b64decode

import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    event_body = json.loads(b64decode(event["body"]))
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = os.environ["RECIPIENT_EMAIL"]

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = os.environ["RECIPIENT_EMAIL"]

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = boto3.session.Session().region_name

    # The subject line for the email.
    SUBJECT = event_body["subject"]

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = event_body["body"]    

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': event_body["email_address"] + ": " + SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
        {
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "statusCode": 500,
            "body": e.response['Error']['Message'],
        }
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        return {
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "statusCode": 200,
            "body": response["MessageId"],
        }
