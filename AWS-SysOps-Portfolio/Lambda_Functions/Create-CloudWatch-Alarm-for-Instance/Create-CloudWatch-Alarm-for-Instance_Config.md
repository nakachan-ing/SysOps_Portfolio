# Create-CloudWatch-Alarm-for-Instanceの設定

## 設定内容
- 関数名: Create-CloudWatch-Alarm-for-Instance
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 60秒

## トリガー
- EventBridgeルール: ルール「EC2-Auto-Scaling-Lunch-Event」は発火し、「EC2 Instance Launch Successful」になったらインスタンスにCloudwatchアラームを作成する

## 環境変数
- 環境変数は設定されていません。

## IAMロール
- Create-CloudWatch-Alarm-for-Instance-role-iuw96bno: Create-CloudWatch-Alarm-for-Instance関数がアクセスできるサービスと権限
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CustomAllow",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricAlarm",
                "ec2:DescribeInstances",
                "cloudwatch:DescribeAlarms",
                "cloudwatch:ListTagsForResource",
                "cloudwatch:TagResource",
                "tag:TagResources"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-northeast-1:********8776:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/Create-CloudWatch-Alarm-for-Instance:*"
            ]
        }
    ]
}
```

## EventBridge ルールの設定

このLambda関数は、EventBridgeのルールによってトリガーされます。以下はその設定に関する情報です。

### ルール名 1
- ルール名: EC2-Auto-Scaling-Lunch-Event
- 説明: EC2 Auto Scalingでインスタンスが起動されたら発火されるルール

### ルールのイベントマッチャー
- イベントパターン:
```json
{
  "source": ["aws.autoscaling"],
  "detail-type": ["EC2 Instance Launch Successful"]
}
```