# EC2-Proc-Rebootの設定

## 設定内容
- 関数名: EC2-Proc-Reboot
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 3秒

## トリガー
- CloudWatchアラーム: アラーム「procstat_lookup_pid_count」のステータスが「ALARM」になったらプロセスを再起動

## 環境変数
- 環境変数は設定されていません。

## IAMロール
- Lambda関数のIAMロール
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup"
            ],
            "Resource": [
                "arn:aws:logs:ap-northeast-1:********8776:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/EC2-Proc-Reboot:*"
            ]
        }
    ]
}
```
- EC2インスタンスのIAMロール
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSendCommand",
            "Effect": "Allow",
            "Action": [
                "ssm:SendCommand",
                "ssm:ListCommands",
                "ssm:ListCommandInvocations"
            ],
            "Resource": "*"
        }
    ]
}
```


## クローン実行に関する注意事項
EC2-Proc-Reboot関数は、単体で実行することが可能。Cronジョブによる定期実行も想定される。詳細な設定内容についてはUsage.mdを参照。