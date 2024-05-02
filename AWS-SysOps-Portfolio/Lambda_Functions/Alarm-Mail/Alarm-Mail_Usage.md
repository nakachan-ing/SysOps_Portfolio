# Alarm-mailの使用方法

## シナリオ1:  Lambda関数「EC2-Alarm-Status-Monitor」実行にともなう関数呼び出しによる実行
- 実行頻度: EC2-Alarm-Status-Monitor実行時（毎日17時）
- 処理内容: EC2-Alarm-Status-Monitorによって取得されたアラーム状況をもとに生成されたメール文を受け取り送信する

## シナリオ2:  他のLambda関数からAlarm-mailを呼び出して実行する場合
- 実行頻度: 他のLambda関数による呼び出しに応じて実行
- 処理内容: 他のLambda関数からAlarm-mailを呼び出すことで、指定されたメール文を送信する
