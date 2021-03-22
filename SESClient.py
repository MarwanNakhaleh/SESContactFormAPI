import boto3

class SESClient:
    def __init__(self):
        region = boto3.session.Session().region_name
        self.client = boto3.client('ses', region_name=region)


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