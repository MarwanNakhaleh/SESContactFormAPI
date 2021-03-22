import boto3

class SESClient:
    def __init__(self, region_name="us-east-1"):
        region = boto3.session.Session().region_name
        if region != None:
            self.client = boto3.client('ses', region_name=region)
        else:
            self.client = boto3.client('ses', region_name=region_name)


    def send_the_email(self, recipient, charset, body_text, email_address, subject):
        return self.client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': charset,
                        'Data': body_text
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': email_address + ": " + subject,
                },
            },
            Source=email_address,
        )
