import boto3
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        text = event['MailText']
        sub = event['Subject']
        Tenant = event['Tenant']
        AlartType = event['AlartType']
        
        print(Tenant)
        print(AlartType)
        
        send_email(os.environ['SEND_ADDRESS'], os.environ['TO_ADDRESS1'], sub, text)
    except ClientError as e:
        print(e)

def send_email(source, to, subject, body):
    client = boto3.client('ses', region_name=os.environ['SEND_REGION'])
    
    client.send_email(
        Source=source,
        Destination={
            'ToAddresses': [to],
        },
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}},
        }
    )
