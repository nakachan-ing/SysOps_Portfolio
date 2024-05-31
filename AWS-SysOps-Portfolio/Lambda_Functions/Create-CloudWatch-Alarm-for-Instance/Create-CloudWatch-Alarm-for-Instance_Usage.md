# Create-CloudWatch-Alarm-for-Instanceの使用方法

## シナリオ1: EventBridgeルールによる定期実行
- 実行頻度: EC2 Auto Scalingでインスタンスが起動された時
- 処理内容: 起動されたインスタンスに対してCloudwatchアラームが作成される
