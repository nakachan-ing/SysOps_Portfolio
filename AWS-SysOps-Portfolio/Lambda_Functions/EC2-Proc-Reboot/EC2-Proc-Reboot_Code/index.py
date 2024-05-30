import os
import boto3
import json
from botocore.exceptions import ClientError

ssm = boto3.client('ssm')

# 対象インスタンス内にある「ProcChk.sh」を実行させる関数
def ssm_send_command(instanceId):
    try:
        res = ssm.send_command( #Systems Managerの処理
            InstanceIds = [
                instanceId,
            ],
            DocumentName = "AWS-RunShellScript",
            Parameters = {
                "commands": [
                    "/opt/shell/ProcChk.sh"
                ],
                "executionTimeout": ["3600"]
            },
        )
        print(res)
    except ClientError as e:
        print(e)


# メイン関数
def lambda_handler(event, context):
    try:
        print(event)
        
        newState = event['detail']['state']['value']                                                    # 今のアラームステータス(ALARM) が取得できる想定
        oldState = event['detail']['previousState']['value']                                            # 前のアラームステータス(OK)が取得できる想定
        metric_name = event['detail']['configuration']['metrics'][0]['metricStat']['metric']['name']    # メトリクス名(procstat_lookup_pid_count)が取得できる想定
        
        print(metric_name)
        
        if newState == "INSUFFICIENT_DATA" and oldState =="OK":                                                                     # (条件1)もし今のアラームステータスが「Alarm」で前のアラームステータスが「OK」なら処理を実行
            if metric_name=="procstat_lookup_pid_count":                                                                            # (条件2)もしメトリクス名が「procstat_lookup_pid_count」なら処理を実行
                instanceId = event['detail']['configuration']['metrics'][0]['metricStat']['metric']['dimensions']['InstanceId']     # アラーム状態のインスタンスIDを取得する
                ssm_send_command(instanceId)                                                                                        # ここでProcChk.shを実行
                     
    except ClientError as e:
        print(e)