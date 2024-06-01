# Start-Aurora-Clusterの設定

## 設定内容
- 関数名: Start-Aurora-Cluster
- ランタイム: Python 3.9
- メモリサイズ: 128MB
- エフェメラルストレージ: 512MB
- タイムアウト: 60秒

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
                "arn:aws:logs:ap-northeast-1:********8776:log-group:/aws/lambda/Start-Aurora-Cluster:*"
            ]
        }
    ]
}
```
- AmazonRDSFullAccess(AWS管理ポリシー)

## EventBridge ルールの設定

このLambda関数は、EventBridgeのルールによってトリガーされます。以下はその設定に関する情報です。

### ルール名 1
- ルール名: StartAuroraCluster-Event
- 説明: Aurora DBクラスターを指定の時間になったら起動するためのルール

### ルールのイベントマッチャー
- イベントパターン:
  ```json
  {
    "source": ["aws.cloudwatch"],
    "detail-type": ["Scheduled Event"],
    "detail": {
        "time": ["cron(0 23 * * ? *)"],
        "resources": ["arn:aws:events:ap-northeast-1:********8776:rule/StartAuroraCluster-Event"]
    }
  }
  ```
