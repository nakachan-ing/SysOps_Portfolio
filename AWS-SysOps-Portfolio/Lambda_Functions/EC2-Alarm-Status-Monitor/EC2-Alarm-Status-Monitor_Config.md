# EC2-Alarm-Status-Monitorの設定

## 設定内容
- 関数名: EC2-Alarm-Status-Monitor
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 3秒

## トリガー
- EventBridgeルール: 毎日17時にEC2インスタンスのアラーム状況を通知する

## 環境変数
- Tenant_Name: "PJMYSELF"

## IAMロール
- EC2-Alarm-Status-Monitor-role-qhqsd66d : EC2-Auto-Start-Stop関数がアクセスできるサービスと権限を持つIAMロール
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "ec2:Describe*",
                    "cloudwatch:GetMetricStatistics",
                    "cloudwatch:Describe*"
                ],
                "Resource": "*"
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": [
                    "lambda:InvokeFunction",
                    "logs:CreateLogGroup"
                ],
                "Resource": [
                    "arn:aws:logs:ap-northeast-1:********8776:*",
                    "arn:aws:lambda:ap-northeast-1:********8776:function:Alarm-mail"
                ]
            },
            {
                "Sid": "VisualEditor2",
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/EC2-Alarm-Status-Monitor:*"
            }
        ]
    }
    ```

## EventBridge ルールの設定

このLambda関数は、EventBridgeのルールによってトリガーされます。以下はその設定に関する情報です。

### ルール名
- ルール名: EC2-Alarm-Status-Monitor-Event
- 説明: EC2インスタンスのアラーム状態を監視するためのルール

### ルールのイベントマッチャー
- イベントパターン:
  ```json
  {
    "source": ["aws.cloudwatch"],
    "detail-type": ["Scheduled Event"],
    "detail": {
        "time": ["cron(0 8 * * ? *)"],
        "resources": ["arn:aws:events:ap-northeast-1:********8776:rule/EC2-Alarm-Status-Monitor-Event"]
    }
  }
  ```
