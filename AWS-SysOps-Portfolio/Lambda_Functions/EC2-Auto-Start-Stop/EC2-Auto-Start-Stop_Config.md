# EC2-Auto-Start-Stopの設定

## 設定内容
- 関数名: EC2-Auto-Start-Stop
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 10秒

## トリガー
- EventBridgeルール: 午前6時になったらEC2インスタンスを停止／午前3時になったらEC2インスタンスを起動

## 環境変数
- 環境変数は設定されていません。

## IAMロール
- EC2-Auto-Start-Stop-role-5lvx37fy: EC2-Auto-Start-Stop関数がアクセスできるサービスと権限を持つIAMロール
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "DescribeInstances",
                "Effect": "Allow",
                "Action": [
                    "ec2:DescribeInstances",
                    "ec2:StartInstances",
                    "ec2:StopInstances"
                ],
                "Resource": "*"
            },
            {
                "Sid": "CreateLogGroup",
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "arn:aws:logs:ap-northeast-1:********8776:*"
            },
            {
                "Sid": "CreateLogStream",
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/EC2-Auto-Start-Stop:*"
            }
        ]
    }
    ```

## EventBridge ルールの設定

このLambda関数は、EventBridgeのルールによってトリガーされます。以下はその設定に関する情報です。

### ルール名 1
- ルール名: EC2-Auto-Start-Event
- 説明: EC2インスタンスを指定の時間になったら起動するためのルール

### ルールのイベントマッチャー
- イベントパターン:
  ```json
  {
    "source": ["aws.cloudwatch"],
    "detail-type": ["Scheduled Event"],
    "detail": {
        "time": ["cron(0 18 * * ? *)"],
        "resources": ["arn:aws:events:ap-northeast-1:********8776:rule/EC2-Auto-Start-Event"]
    }
  }
  ```

### 入力定数
```json
{
  "Action": "start"
}
```

### ルール名 2
- ルール名: EC2-Auto-Stop-Event
- 説明: EC2インスタンスを指定の時間になったら停止するためのルール

### ルールのイベントマッチャー
- イベントパターン:
  ```json
  {
    "source": ["aws.cloudwatch"],
    "detail-type": ["Scheduled Event"],
    "detail": {
        "time": ["cron(0 21 * * ? *)"],
        "resources": ["arn:aws:events:ap-northeast-1:********8776:rule/EC2-Auto-Stop-Event"]
    }
  }
  ```

### 入力定数
```json
{
  "Action": "stop"
}
```