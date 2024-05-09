import boto3
import os
import shutil
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import matplotlib.pyplot as plt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# AWSクライアントの初期化
ec2 = boto3.client('ec2')
cloudWatch = boto3.client('cloudwatch')
ses = boto3.client('ses', region_name=os.environ['SEND_REGION'])

# 環境変数からテナント名を取得
tenant = os.environ['TENANT']

# CSVと画像用のディレクトリ作成
csv_dir = f'/tmp/folder/csv'
img_dir = f'/tmp/folder/{tenant}_img'
os.makedirs(csv_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

# ファイルパス
csv_file = f'{csv_dir}/{tenant}_metrics_data.csv'
summary_csv_file = f'{csv_dir}/{tenant}_metrics_summary_data.csv'
zip_file = f'/tmp/{tenant}_folder.zip'

def lambda_handler(event, context):
    try:
        # CSVファイルをヘッダー付きで初期化
        init_csv(summary_csv_file, ["alarm_name", "alarm_status", "Max", "Avg"])

        # インスタンスIDを取得
        instance_IDs = describe_instanceIDs()

        # 各インスタンスを処理
        for instance_ID in instance_IDs:
            tag_name = get_instance_tag_name(instance_ID)
            describe_Alarm_status(instance_ID, tag_name, csv_file)

        # ZIPアーカイブを作成
        shutil.make_archive(f'/tmp/{tenant}_folder', 'zip', root_dir='/tmp/folder')

        # メールを添付して送信
        send_email(zip_file)

        return "Success"

    except Exception as e:
        print(e)
        return "Error"

def init_csv(file_path, headers):
    with open(file_path, "w") as file:
        file.write(",".join(headers) + '\n')

def describe_instanceIDs():
    response = ec2.describe_instances()
    instance_IDs = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    return instance_IDs

def get_instance_tag_name(instance_ID):
    tags_info = ec2.describe_instances(Filters=[
        {'Name': 'tag-key', 'Values':['Name']},
        {'Name': 'instance-id', 'Values':[instance_ID]}
    ])['Reservations'][0]['Instances'][0]['Tags']

    for tag in tags_info:
        if tag['Key'] == "Name":
            return tag['Value']

def describe_Alarm_status(instance_ID, tag_name, csv_file):
    alarm_list = cloudWatch.describe_alarms(AlarmNamePrefix=tag_name)['MetricAlarms']

    for alarm in alarm_list:
        alarm_name = alarm['AlarmName']
        alarm_status = alarm['StateValue']
        df, max_values, avg_values = get_alarm_value(alarm)
        df.to_csv(csv_file, mode='a')
        save_max_fig(df, alarm)
        save_avg_fig(df, alarm)
        save_summary_csv(alarm_name, alarm_status, max(max_values, default="None"), sum(avg_values) / len(avg_values) if avg_values else "None")

def get_alarm_value(alarm):
    end_time = datetime.datetime.now() - relativedelta(days=1)
    start_time = end_time - relativedelta(months=1)
    response = cloudWatch.get_metric_statistics(
        Namespace=alarm['Namespace'],
        MetricName=alarm['MetricName'],
        Dimensions=alarm['Dimensions'],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=['Average', 'Maximum']
    )
    data = response['Datapoints']
    if data:
        df = pd.DataFrame(data)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df = df.set_index('Timestamp').sort_index(ascending=True)
        return df, df['Maximum'].tolist(), df['Average'].tolist()
    else:
        return pd.DataFrame(), [], []

def save_max_fig(df, alarm):
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['Maximum'])
    plt.xlabel('Date')
    plt.ylabel('Usage(%)')
    plt.title(alarm['AlarmName'] + '_max')
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig(os.path.join(img_dir, f"{alarm['AlarmName']}_max.jpg"))
    plt.close()

def save_avg_fig(df, alarm):
    plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['Average'])
    plt.xlabel('Date')
    plt.ylabel('Usage(%)')
    plt.title(alarm['AlarmName'] + '_avg')
    plt.ticklabel_format(style='plain', axis='y')
    plt.savefig(os.path.join(img_dir, f"{alarm['AlarmName']}_avg.jpg"))
    plt.close()

def save_summary_csv(alarm_name, alarm_status, max_value, avg_value):
    with open(summary_csv_file, "a") as file:
        file.write(f"{alarm_name},{alarm_status},{max_value},{avg_value}\n")

def send_email(attachment_path):
    msg = MIMEMultipart()
    msg['Subject'] = "Metrics Notification"
    msg['From'] = os.environ['FROM_ADDRESS']
    msg['To'] = os.environ['TO_ADDRESS']
    body = f"Metrics report for {tenant} from {datetime.datetime.now() - relativedelta(months=1)} to {datetime.datetime.now() - relativedelta(days=1)}"
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, "rb") as attachment:
        att = MIMEApplication(attachment.read())
        att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
        msg.attach(att)

    ses.send_raw_email(
        Source=os.environ['FROM_ADDRESS'],
        Destinations=[os.environ['TO_ADDRESS']],
        RawMessage={'Data': msg.as_string()}
    )
