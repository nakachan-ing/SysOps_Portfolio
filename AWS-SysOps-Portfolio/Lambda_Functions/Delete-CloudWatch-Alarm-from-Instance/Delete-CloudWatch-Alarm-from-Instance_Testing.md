# Delete-CloudWatch-Alarm-from-Instanceのテスト

## テストケース1: EventBridgeルールによる定期実行の検証
- 実行タイミング: EC2 Auto Scalingでインスタンスが終了された時
- 処理内容: 終了したインスタンスのCloudwatchアラームが削除されていることを確認
