import boto3
import os
import json
from botocore.exceptions import ClientError
import datetime

ec2 = boto3.client('ec2', region_name='ap-northeast-1')

def lambda_handler(event, context):
    try:
        # イベントの内容をログに出力
        print(event['Action'])

        # イベントに応じてインスタンスの起動または停止を行う
        if event['Action'] == 'stop':
            stop_instances()
            print('インスタンスを停止しました。')
        elif event['Action'] == 'start':            
            start_instances()
            print('インスタンスを起動しました。')
        else:
            pass

    except ClientError as e:
        print(e)


def stop_instances():
    # EC2インスタンスをすべて停止する
    all_list = describe_instanceIds()
    ec2.stop_instances(InstanceIds=all_list)

def start_instances():
    # EC2インスタンスをすべて起動する
    all_list = describe_instanceIds()
    ec2.start_instances(InstanceIds=all_list)

def describe_instanceIds():
    # すべてのEC2インスタンスIDを取得する
    all_list = []
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instanceId = instance['InstanceId']
            all_list.append(instanceId)
    return all_list
