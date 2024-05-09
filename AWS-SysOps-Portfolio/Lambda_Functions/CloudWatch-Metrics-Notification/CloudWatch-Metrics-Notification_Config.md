## CloudWatch-Metrics-NotificationのConfig

- **関数名**: CloudWatch-Metrics-Notification
- **ランタイム**: Python 3.9
- **メモリサイズ**: 128MB 以上推奨
- **エフェメラルストレージ**: 512MB 以上推奨
- **タイムアウト**: 10秒以上推奨

### トリガー

このLambda関数は、定期的に実行することを想定しています。具体的なトリガーは以下の通りです。

- **トリガー種別**: CloudWatch Events ルール
- **実行スケジュール**: ユーザーが設定したスケジュールに基づき、例えば毎日または毎週など

### 環境変数

このLambda関数を実行するために、以下の環境変数を設定する必要があります。

- `SEND_REGION`: SESのリージョン名
- `TENANT`: テナント名
- `FROM_ADDRESS`: 送信元メールアドレス
- `TO_ADDRESS1`: 送信先メールアドレス（複数の場合はカンマ区切り）

### IAMロール

Lambda関数が必要な権限を持つIAMロールが必要です。特に以下の権限が必要です。

- `ec2:DescribeInstances`: EC2インスタンスの情報を取得するため
- `cloudwatch:DescribeAlarms`: CloudWatchアラームの情報を取得するため
- `cloudwatch:GetMetricStatistics`: メトリクスの統計情報を取得するため
- `ses:SendRawEmail`: SESを使用してメールを送信するため
