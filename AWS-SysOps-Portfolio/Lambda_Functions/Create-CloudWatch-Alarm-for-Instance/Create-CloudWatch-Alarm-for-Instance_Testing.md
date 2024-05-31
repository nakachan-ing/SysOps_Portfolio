# Create-CloudWatch-Alarm-for-Instanceのテスト

## テストケース1: EventBridgeルールによる定期実行の検証
- 実行タイミング: EC2 Auto Scalingでインスタンスが起動された時
- 処理内容: 起動されたインスタンスに対してCloudwatchアラームが作成されていることを確認
