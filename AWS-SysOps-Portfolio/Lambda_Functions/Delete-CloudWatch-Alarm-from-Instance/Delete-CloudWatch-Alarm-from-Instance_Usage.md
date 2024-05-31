# Delete-CloudWatch-Alarm-from-Instanceの使用方法

## シナリオ1: EventBridgeルールによる定期実行
- 実行頻度: EC2 Auto Scalingでインスタンスが終了した時
- 処理内容: 終了したインスタンスのCloudwatchアラームが削除される
