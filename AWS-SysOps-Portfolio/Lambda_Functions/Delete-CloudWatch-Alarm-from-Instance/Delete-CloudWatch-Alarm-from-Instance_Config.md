# Delete-CloudWatch-Alarm-from-Instanceの設定

## 設定内容
- 関数名: Delete-CloudWatch-Alarm-from-Instance
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 3秒

## トリガー
- EventBridgeルール: ルール「EC2-Auto-Scaling-Terminate-Event」が発火し、「EC2 Instance Terminate Successful」になったらインスタンスのCloudwatchアラームを削除する

## 環境変数
- 環境変数は設定されていません。

## IAMロール
- Delete-CloudWatch-Alarm-from-Instance-role-15uhacaf: Delete-CloudWatch-Alarm-from-Instance関数がアクセスできるサービスと権限
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowDeleteAlarms",
            "Effect": "Allow",
            "Action": "cloudwatch:*",
            "Resource": "*"
        },
        {
            "Sid": "DefaultAllow1",
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-northeast-1:********8776:*"
        },
        {
            "Sid": "DefaultAllow2",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/Delete-CloudWatch-Alarm-from-Instance:*"
        }
    ]
}
```

## EventBridge ルールの設定

このLambda関数は、EventBridgeのルールによってトリガーされます。以下はその設定に関する情報です。

### ルール名 1
- ルール名: EC2-Auto-Scaling-Lunch-Event
- 説明: EC2 Auto Scalingでインスタンスが終了したら発火されるルール

### ルールのイベントマッチャー
- イベントパターン:
```json
{
  "source": ["aws.autoscaling"],
  "detail-type": ["EC2 Instance Terminate Successful"]
}
```