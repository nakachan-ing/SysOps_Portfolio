# EC2-Proc-Rebootの使用方法

## シナリオ1: CloudWatchアラームのステータス変更のイベントによる実行
- 実行頻度: アラーム「procstat_lookup_pid_count」のステータスが「ALARM」になったとき
- 処理内容: アラーム対象のプロセスが見つかった場合、Lambda関数がEC2インスタンス内の「ProcChk.sh」スクリプトを実行して、該当プロセスを再起動。この際、EC2-Proc-Reboot関数が特定のコマンドを実行するためのIAMロールが必要。

## 定期実行方法
ProcChk.shはCronジョブによって定期的に実行可能。以下のようにCron設定。
```cron
# 毎時0分にProcChk.shを実行
0 * * * * /bin/bash /path/to/ProcChk.sh
```

## 単体実行方法
ProcChk.shはCronジョブによって定期的に実行されることが想定されるが、単体でも実行可能。以下のコマンドを使用して単体で実行可能。
```bash
bash ProcChk.sh
```

