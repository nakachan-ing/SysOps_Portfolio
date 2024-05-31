import boto3
from botocore.exceptions import ClientError

cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')
tag_client = boto3.client('resourcegroupstaggingapi')

def create_disk_usage_alarm(instance_id, instance_type, device, fstype, path):
    try:
        alarm_name = f"DiskUsage-{instance_id}-{device}-{path}"
        cloudwatch.put_metric_alarm(
            AlarmName=alarm_name,
            AlarmDescription=f"Alarm for disk usage on instance {instance_id} for device {device} and path {path}",
            ActionsEnabled=True,
            AlarmActions=[],  # アラームがトリガーされたときのアクションを設定
            MetricName='disk_used_percent',
            Namespace='CWAgent',
            Statistic='Average',
            Period=300,  # 5 minutes
            EvaluationPeriods=1,
            Threshold=80.0,
            ComparisonOperator='GreaterThanThreshold',
            Dimensions=[
                {'Name': 'InstanceId', 'Value': instance_id},
                {'Name': 'InstanceType', 'Value': instance_type},
                {'Name': 'device', 'Value': device},
                {'Name': 'fstype', 'Value': fstype},
                {'Name': 'path', 'Value': path}
            ],
        Unit='Percent'
        )
        add_tags_to_alarm(alarm_name)
    except ClientError as e:
        print(e)

def create_memory_usage_alarm(instance_id, instance_type):
    try:
        alarm_name = f"MemoryUsage-{instance_id}"
        cloudwatch.put_metric_alarm(
            AlarmName=alarm_name,
            AlarmDescription=f"Alarm for memory usage on instance {instance_id}",
            ActionsEnabled=True,
            AlarmActions=[],  # アラームがトリガーされたときのアクションを設定
            MetricName='mem_used_percent',
            Namespace='CWAgent',
            Statistic='Average',
            Period=300,  # 5 minutes
            EvaluationPeriods=1,
            Threshold=80.0,
            ComparisonOperator='GreaterThanThreshold',
            Dimensions=[
                {'Name': 'InstanceId', 'Value': instance_id},
                {'Name': 'InstanceType', 'Value': instance_type}
            ],
            Unit='Percent'
        )
        add_tags_to_alarm(alarm_name)
    except ClientError as e:
        print(e)

def create_process_pid_count_alarm(instance_id, instance_type, pidfile, pid_finder):
    try:
        alarm_name = f"ProcessPIDCount-{instance_id}"
        cloudwatch.put_metric_alarm(
            AlarmName=alarm_name,
            AlarmDescription=f"Alarm for process PID count on instance {instance_id}",
            ActionsEnabled=True,
            AlarmActions=[],  # アラームがトリガーされたときのアクションを設定
            MetricName='procstat_lookup_pid_count',
            Namespace='CWAgent',
            Statistic='Average',
            Period=60,  # 1 minutes
            EvaluationPeriods=1,
            Threshold=1.0,
            ComparisonOperator='LessThanThreshold',
            Dimensions=[
                {'Name': 'InstanceId', 'Value': instance_id},
                {'Name': 'InstanceType', 'Value': instance_type},
                {'Name': 'pidfile', 'Value': pidfile},
                {'Name': 'pid_finder', 'Value': pid_finder}
            ],
            TreatMissingData='breaching'
        )
        add_tags_to_alarm(alarm_name)
    except ClientError as e:
        print(e)

def add_tags_to_alarm(alarm_name):
    try:
        region = boto3.Session().region_name
        account_id = boto3.client("sts").get_caller_identity()["Account"]
        alarm_arn = f'arn:aws:cloudwatch:{region}:{account_id}:alarm:{alarm_name}'
        
        tag_client.tag_resources(
            ResourceARNList=[alarm_arn],
            Tags = {
                'aws-exam-resource': 'true'
            }
        )
        print(f"Successfully tagged the alarm: {alarm_name}")
    except Exception as e:
        print(f"Failed to tag the alarm: {alarm_name}. Error: {e}")


def lambda_handler(event, context):
    try:
        instance_id = event['detail']['EC2InstanceId']
    
        # インスタンスタイプを取得
        instance_info = ec2.describe_instances(InstanceIds=[instance_id])
        instance_type = instance_info['Reservations'][0]['Instances'][0]['InstanceType']
        
        # ディスクデバイスとファイルシステムの情報
        disk_devices = [
            {"device": "xvda1", "fstype": "xfs", "path": "/"},
            {"device": "tmpfs", "fstype": "tmpfs", "path": "/run"}
        ]
        
        for disk in disk_devices:
            create_disk_usage_alarm(instance_id, instance_type, disk['device'], disk['fstype'], disk['path'])
        
        create_memory_usage_alarm(instance_id, instance_type)
        
        pidfile = "/run/nginx.pid"
        pid_finder = "native"
        
        create_process_pid_count_alarm(instance_id, instance_type, pidfile, pid_finder)
    
        return {
            'statusCode': 200,
            'body': f'Alarms created for instance {instance_id}'
        }
    except ClientError as e:
        print(e)