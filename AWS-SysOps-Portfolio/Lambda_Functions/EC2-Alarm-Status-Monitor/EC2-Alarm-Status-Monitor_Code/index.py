import boto3
import os
import json
from botocore.exceptions import ClientError
import datetime
from dateutil.relativedelta import relativedelta

ec2 = boto3.client('ec2')
cloudWatch = boto3.client('cloudwatch')

def describe_instanceIDs():     #インスタンスIDを取得
    try:
        all_list = []   ##すべてのインスタンスIDを取得
        
        responce = ec2.describe_instances()
        for reservation in responce['Reservations']:
            for instance in reservation['Instances']:
                all_list.append(instance['InstanceId'])
        return all_list        
    except ClientError as e:
         print(e)


def get_instance_tag_name(instance_ID):
    tags_info = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag-key',
                'Values':['Name']
            },
            {
                'Name': 'instance-id',
                'Values':[instance_ID]
            }
        ]
    )['Reservations'][0]['Instances'][0]['Tags']
    for res in tags_info :
        if res['Key'] == "Name":
            tag_name = res['Value']
            return tag_name


def create_mail_text(instance_ID, tag_name, Tenant):    #メール本文の内容を決定
    text = '\n' + "・" + tag_name + '\n'
    alarm_list = cloudWatch.describe_alarms(
        AlarmNamePrefix= tag_name
    )['MetricAlarms']

    text += describe_Alarm_status(alarm_list,instance_ID)
    
    print(alarm_list)
    return text


def describe_Alarm_status(alarm_list, instance_ID):     #各サーバーのアラーム内容を追記
    text = ""
    i = 0
    for alarmList in alarm_list:
        i += 1
        alarm_name = alarmList['AlarmName']
        alarm_status = alarmList['StateValue']
        for dimensions in alarmList['Dimensions']:
            if str(dimensions['Value']) == str(instance_ID):
                if alarm_status == "INSUFFICIENT_DATA":
                    text += alarm_name + " >> " + alarm_status + '\n'
                else:
                    max_list = get_alarm_value(alarmList, i)
                    max_value = max(max_list)
                    text += alarm_name + " >> " + alarm_status + "  値：" + str(max_value) + '\n'
    return text


def get_alarm_value(alarmList, i):
    max_list = []

    alarm_value = cloudWatch.get_metric_statistics(
        Namespace = alarmList['Namespace'],
        MetricName = alarmList['MetricName'],
        Dimensions = alarmList['Dimensions'],
        StartTime = datetime.datetime.now() - relativedelta(days=1) + datetime.timedelta(hours=9),
        EndTime = datetime.datetime.now() + datetime.timedelta(hours=9),
        Period = 1800,    ## 取得間隔は30分(60*30)
        Statistics = [
             'Maximum',
        ]
    )

    if len(alarm_value) != 0:
        for value in alarm_value['Datapoints']:
            max_list.append(value['Maximum'])
    return max_list
    

def lambda_handler(event, context):
    try:
        Tenant = os.environ['Tenant_Name']
        text = Tenant + "のサーバーのアラーム状況" + '\n'

        instance_IDs = describe_instanceIDs()

        for instance_ID in instance_IDs:
            tag_name = get_instance_tag_name(instance_ID)
            text += create_mail_text(instance_ID, tag_name, Tenant)
            sub = Tenant + '-EC2-Alarm-status-monitor'
        send_email(text, sub, Tenant)
    except ClientError as e:
        print(e)
        

def send_email(text,sub,Tenant):
    params = {
        'MailText' : text,
        'Subject' : sub,
        'Tenant' : Tenant,
        'AlartType' : 'Alarm-Status-monitor'
    }

    res = boto3.client('lambda').invoke(
        FunctionName='arn:aws:lambda:ap-northeast-1:********8776:function:Alarm-mail',
        InvocationType = 'Event', 
        Payload = json.dumps(params)
    )

    print("メール送信")