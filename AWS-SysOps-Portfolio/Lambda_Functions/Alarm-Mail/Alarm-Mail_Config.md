# Alarm-mailの設定

## 設定内容
- 関数名: Alarm-mail
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 3秒

## トリガー
- Lambda関数: 任意のLambda関数内で「Alarm-mail」が呼び出された際、生成されたメール文を宛先に送信する

## 環境変数
- `SEND_ADDRESS`: 送信元のメールアドレス
- `TO_ADDRESS`: 送信先のメールアドレス
- `SEND_REGION`: メール送信リージョン

## IAMロール
- ロール名: Alarm-mail-role-t2lst202
- ロールの目的: Alarm-mail関数がアクセス可能なサービスと権限を持つIAMロール

IAMロールのポリシー:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreateLogGroup",
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-northeast-1:********8776:*"
        },
        {
            "Sid": "PutLogEvents",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/Alarm-mail:*"
        },
        {
            "Sid": "AllowEmailSending",
            "Effect": "Allow",
            "Action": "ses:SendEmail",
            "Resource": "*"
        }
    ]
}
```