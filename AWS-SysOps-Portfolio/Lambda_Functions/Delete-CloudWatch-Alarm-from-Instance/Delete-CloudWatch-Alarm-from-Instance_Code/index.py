import boto3
import json
from botocore.exceptions import ClientError

cloudwatch = boto3.client('cloudwatch')

def delete_alarms_for_instance(instance_id):
    try:
        paginator = cloudwatch.get_paginator('describe_alarms')
        for page in paginator.paginate():
            for alarm in page['MetricAlarms']:
                if any(d['Name'] == 'InstanceId' and d['Value'] == instance_id for d in alarm['Dimensions']):
                    alarm_name = alarm['AlarmName']
                    print(f"Deleting alarm: {alarm_name}")
                    cloudwatch.delete_alarms(AlarmNames=[alarm_name])
    except ClientError as e:
        print(e)

def lambda_handler(event, context):
    detail = event.get('detail', {})
    instance_id = detail.get('EC2InstanceId', '')

    if not instance_id:
        return {
            'statusCode': 400,
            'body': 'No EC2InstanceId found in the event'
        }

    delete_alarms_for_instance(instance_id)

    return {
        'statusCode': 200,
        'body': f'Alarms deleted for instance {instance_id}'
    }
